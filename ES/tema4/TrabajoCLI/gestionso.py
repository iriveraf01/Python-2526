import time
import argparse
from control import control_cpu, control_mem, control_disk, control_temp, control_net


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
        help="Mostrar logs por pantalla"
    )

    args = parser.parse_args()

    while True:
        control_cpu(mostrar=args.screen, umbral=args.cpu)
        control_mem(mostrar=args.screen)
        control_disk(mostrar=args.screen, umbral=args.disk)
        control_temp(mostrar=args.screen, umbral=args.temp)
        control_net(mostrar=args.screen, puertos_permitidos=args.puertos)

        time.sleep(5)


if __name__ == "__main__":
    main()