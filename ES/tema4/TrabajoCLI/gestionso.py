import time
import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live

from checks import cpu_met, memory_met, disk_met, temperatures_met, net_met
from control import control_cpu, control_mem, control_disk, control_temp, control_net

console = Console()


def construir_pantalla():
    cpu = cpu_met()
    mem = memory_met()
    disk = disk_met()
    temp = temperatures_met()
    net = net_met()

    tabla = Table(title="Monitorización del Sistema", expand=True)

    tabla.add_column("Métrica", justify="left", style="cyan", no_wrap=True)
    tabla.add_column("Valor", justify="left", style="magenta")

    tabla.add_row("CPU", f"{cpu['cpu_percent']}%")
    tabla.add_row("RAM", f"{mem['ram']['percent']}%")
    tabla.add_row("SWAP", f"{mem['swap']['percent']}%")
    tabla.add_row("DISCO", f"{disk['percent']}%")
    tabla.add_row("CONEXIONES", str(net["total_connections"]))
    tabla.add_row("PUERTOS ABIERTOS", str(len(net["listening_ports"])))

    # Temperatura máxima si existe
    max_temp = "No disponible"
    temps = temp["temperatures"]
    if temps:
        mayor = 0
        for sensor in temps.values():
            for entry in sensor:
                if entry["current"] and entry["current"] > mayor:
                    mayor = entry["current"]
        if mayor > 0:
            max_temp = f"{mayor}°C"

    tabla.add_row("TEMPERATURA", max_temp)
    tabla.add_row("HORA", cpu["timestamp"])

    return Panel(tabla, title="CLI Monitor", border_style="green")


def main():
    parser = argparse.ArgumentParser(
        description="Monitorización del sistema con logs y alertas"
    )

    parser.add_argument(
        "-p", "--puertos",
        nargs="*",
        type=int,
        default=[],
        help="Lista de puertos permitidos que no generan aviso"
    )

    parser.add_argument(
        "-c", "--cpu",
        type=float,
        default=80,
        help="Umbral de aviso para CPU"
    )

    parser.add_argument(
        "-t", "--temp",
        type=float,
        default=80,
        help="Umbral de aviso para temperatura"
    )

    parser.add_argument(
        "-d", "--disk",
        type=float,
        default=80,
        help="Umbral de aviso para disco"
    )

    parser.add_argument(
        "-s", "--screen",
        action="store_true",
        help="Mostrar interfaz por pantalla"
    )

    args = parser.parse_args()

    if args.screen:
        with Live(construir_pantalla(), refresh_per_second=1, console=console) as live:
            while True:
                control_cpu(mostrar=False, umbral=args.cpu)
                control_mem(mostrar=False)
                control_disk(mostrar=False, umbral=args.disk)
                control_temp(mostrar=False, umbral=args.temp)
                control_net(mostrar=False, puertos_permitidos=args.puertos)

                live.update(construir_pantalla())
                time.sleep(5)
    else:
        while True:
            control_cpu(mostrar=False, umbral=args.cpu)
            control_mem(mostrar=False)
            control_disk(mostrar=False, umbral=args.disk)
            control_temp(mostrar=False, umbral=args.temp)
            control_net(mostrar=False, puertos_permitidos=args.puertos)

            time.sleep(5)


if __name__ == "__main__":
    main()