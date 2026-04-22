import psutil
import shutil
from datetime import datetime


def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def cpu_met():
    """
    Devuelve métricas básicas de CPU.
    """
    return {
        "timestamp": _timestamp(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "cpu_count_physical": psutil.cpu_count(logical=False),
        "load_avg": getattr(psutil, "getloadavg", lambda: None)()
    }


def memory_met():
    """
    Devuelve información de RAM y SWAP.
    """
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return {
        "timestamp": _timestamp(),
        "ram": {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "percent": mem.percent
        },
        "swap": {
            "total": swap.total,
            "used": swap.used,
            "free": swap.free,
            "percent": swap.percent,
            "sin": getattr(swap, "sin", None),
            "sout": getattr(swap, "sout", None)
        }
    }


def disk_met(path="/"):
    """
    Devuelve uso de disco de una ruta.
    Por defecto, la raíz del sistema.
    """
    usage = psutil.disk_usage(path)

    return {
        "timestamp": _timestamp(),
        "path": path,
        "total": usage.total,
        "used": usage.used,
        "free": usage.free,
        "percent": usage.percent
    }


def temperatures_met():
    """
    Devuelve temperaturas detectadas por el sistema.
    En algunos sistemas puede no haber datos.
    """
    try:
        temps = psutil.sensors_temperatures()
    except (AttributeError, NotImplementedError):
        temps = {}

    resultado = {
        "timestamp": _timestamp(),
        "temperatures": {}
    }

    for sensor_name, entries in temps.items():
        resultado["temperatures"][sensor_name] = []
        for entry in entries:
            resultado["temperatures"][sensor_name].append({
                "label": entry.label,
                "current": entry.current,
                "high": entry.high,
                "critical": entry.critical
            })

    return resultado


def net_met():
    """
    Devuelve conexiones de red y puertos en escucha.
    """
    conexiones = psutil.net_connections(kind="inet")
    escuchando = []

    for conn in conexiones:
        if conn.status == psutil.CONN_LISTEN and conn.laddr:
            escuchando.append({
                "ip": conn.laddr.ip,
                "port": conn.laddr.port,
                "pid": conn.pid
            })

    return {
        "timestamp": _timestamp(),
        "listening_ports": escuchando,
        "total_connections": len(conexiones)
    }