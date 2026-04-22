from datetime import datetime, timedelta

from dotenv import load_dotenv
from checks import cpu_met, memory_met, disk_met, temperatures_met, net_met
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CPU_INTERVAL = 10
MEM_INTERVAL = 15
DISK_INTERVAL = 30
TEMP_INTERVAL = 20
NET_INTERVAL = 25

last_cpu = None
last_mem = None
last_disk = None
last_temp = None
last_net = None

# Banderas para no repetir alertas continuamente
cpu_alerta_activa = False
mem_alerta_activa = False
disk_alerta_activa = False
temp_alerta_activa = False
net_alerta_activa = False
    

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def escribir_log(nombre_fichero, mensaje):
    ruta = os.path.join(BASE_DIR, nombre_fichero)
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(mensaje + "\n")


def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    datos = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }

    try:
        respuesta = requests.post(url, data=datos, timeout=2)
        return respuesta.status_code == 200
    except requests.RequestException:
        return False


def control_cpu(mostrar=False, intervalo=CPU_INTERVAL, umbral=80):
    global last_cpu, cpu_alerta_activa

    ahora = datetime.now()

    if last_cpu is None or (ahora - last_cpu) >= timedelta(seconds=intervalo):
        datos = cpu_met()
        cpu = datos["cpu_percent"]

        mensaje = f"[{datos['timestamp']}] CPU: {cpu}%"

        if mostrar:
            print(mensaje)

        escribir_log("log_cpu.txt", mensaje)

        if cpu > umbral:
            if not cpu_alerta_activa:
                aviso = f"[{datos['timestamp']}] ⚠️ ALERTA CPU: {cpu}%"

                if mostrar:
                    print(aviso)

                escribir_log("log_cpu.txt", aviso)

                enviado = enviar_telegram(aviso)
                if mostrar:
                    print("Mensaje enviado a Telegram" if enviado else "No se pudo enviar el mensaje a Telegram")

                cpu_alerta_activa = True
        else:
            cpu_alerta_activa = False

        last_cpu = ahora


def control_mem(mostrar=False, intervalo=MEM_INTERVAL):
    global last_mem, mem_alerta_activa

    ahora = datetime.now()

    if last_mem is None or (ahora - last_mem) >= timedelta(seconds=intervalo):
        datos = memory_met()
        ram = datos["ram"]["percent"]
        swap = datos["swap"]["percent"]

        mensaje = f"[{datos['timestamp']}] MEM: RAM {ram}% | SWAP {swap}%"

        if mostrar:
            print(mensaje)

        escribir_log("log_mem.txt", mensaje)

        if ram > 80 and swap > 20:
            if not mem_alerta_activa:
                aviso = f"[{datos['timestamp']}] ⚠️ ALERTA MEMORIA: RAM {ram}% | SWAP {swap}%"

                if mostrar:
                    print(aviso)

                escribir_log("log_mem.txt", aviso)

                enviado = enviar_telegram(aviso)
                if mostrar:
                    print("Mensaje enviado a Telegram" if enviado else "No se pudo enviar el mensaje a Telegram")

                mem_alerta_activa = True
        else:
            mem_alerta_activa = False

        last_mem = ahora


def control_disk(mostrar=False, intervalo=DISK_INTERVAL, umbral=80):
    global last_disk, disk_alerta_activa

    ahora = datetime.now()

    if last_disk is None or (ahora - last_disk) >= timedelta(seconds=intervalo):
        datos = disk_met()
        uso = datos["percent"]

        mensaje = f"[{datos['timestamp']}] DISK: {uso}%"

        if mostrar:
            print(mensaje)

        escribir_log("log_disk.txt", mensaje)

        if uso > umbral:
            if not disk_alerta_activa:
                aviso = f"[{datos['timestamp']}] ⚠️ ALERTA DISCO: {uso}%"

                if mostrar:
                    print(aviso)

                escribir_log("log_disk.txt", aviso)

                enviado = enviar_telegram(aviso)
                if mostrar:
                    print("Mensaje enviado a Telegram" if enviado else "No se pudo enviar el mensaje a Telegram")

                disk_alerta_activa = True
        else:
            disk_alerta_activa = False

        last_disk = ahora


def control_temp(mostrar=False, intervalo=TEMP_INTERVAL, umbral=80):
    global last_temp, temp_alerta_activa

    ahora = datetime.now()

    if last_temp is None or (ahora - last_temp) >= timedelta(seconds=intervalo):
        datos = temperatures_met()
        temps = datos["temperatures"]

        if not temps:
            mensaje = f"[{datos['timestamp']}] TEMP: No disponible"

            if mostrar:
                print(mensaje)

            escribir_log("log_temp.txt", mensaje)
            last_temp = ahora
            temp_alerta_activa = False
            return

        max_temp = 0

        for sensor in temps.values():
            for entry in sensor:
                if entry["current"] is not None and entry["current"] > max_temp:
                    max_temp = entry["current"]

        mensaje = f"[{datos['timestamp']}] TEMP: {max_temp}°C"

        if mostrar:
            print(mensaje)

        escribir_log("log_temp.txt", mensaje)

        if max_temp > umbral:
            if not temp_alerta_activa:
                aviso = f"[{datos['timestamp']}] ⚠️ ALERTA TEMPERATURA: {max_temp}°C"

                if mostrar:
                    print(aviso)

                escribir_log("log_temp.txt", aviso)

                enviado = enviar_telegram(aviso)
                if mostrar:
                    print("Mensaje enviado a Telegram" if enviado else "No se pudo enviar el mensaje a Telegram")

                temp_alerta_activa = True
        else:
            temp_alerta_activa = False

        last_temp = ahora


def control_net(mostrar=False, intervalo=NET_INTERVAL, puertos_permitidos=None):
    global last_net, net_alerta_activa

    if puertos_permitidos is None:
        puertos_permitidos = []

    ahora = datetime.now()

    if last_net is None or (ahora - last_net) >= timedelta(seconds=intervalo):
        datos = net_met()
        puertos = datos["listening_ports"]

        mensaje = f"[{datos['timestamp']}] NET: {len(puertos)} puertos abiertos"

        if mostrar:
            print(mensaje)

        escribir_log("log_net.txt", mensaje)

        puertos_alerta = [p for p in puertos if p["port"] not in puertos_permitidos]

        if puertos_alerta:
            lista_puertos = ", ".join(str(p["port"]) for p in puertos_alerta[:10])
            aviso = f"[{datos['timestamp']}] ⚠️ ALERTA RED: Puertos no permitidos detectados: {lista_puertos}"

            if not net_alerta_activa:
                if mostrar:
                    print(aviso)

                escribir_log("log_net.txt", aviso)

                enviado = enviar_telegram(aviso)
                if mostrar:
                    print("Mensaje enviado a Telegram" if enviado else "No se pudo enviar el mensaje a Telegram")

                net_alerta_activa = True
        else:
            net_alerta_activa = False

        last_net = ahora