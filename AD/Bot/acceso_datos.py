import pandas as pd
from influxdb import InfluxDBClient


HOST = '10.0.0.8'
PORT = 8886
USER = 'pythonread'
PASS = 'read1234'
DB = 'agro_sensex'

def ping():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    print("Prueba de conexión")
    ping_result = client.ping()
    if ping_result:
        print(ping_result)
    else:
        print("No conectado")

def consulta_bbdd():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    print("\nMostrando las bases de datos")
    databases = client.get_list_database()
    for i in databases:
        print(i['name'])

def consultar_tablas():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    print(f"\nMostrando tablas de la BD ({DB})")
    respuesta = client.query("SHOW MEASUREMENTS")
    points = list(respuesta.get_points())
    print(f"Existen {len(points)} measurements")
    for i in points:
        print(i['name'])

def consultar_tag_key():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    print("\nMostrando columnas de tipo TAG")
    respuesta = client.query('SHOW TAG KEYS FROM "%"')
    points = list(respuesta.get_points())
    print(f"Existen {len(points)} columnas de tipo TAG en la tabla %")
    for i in points:
        print(i)

def consultar_tag_values():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    print("\nMostrando valores únicos de la columna entity_id")
    respuesta = client.query('SHOW TAG VALUES FROM "%" WITH KEY = "entity_id"')
    points = list(respuesta.get_points())
    print(f"Existen {len(points)} valores únicos")
    for i in points:
        print(i)

def consultar_fields():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    print("\nMostrando las columnas tipo field de %")
    respuesta = client.query('SHOW FIELD KEYS FROM "%"')
    points = list(respuesta.get_points())
    print(f"Existen {len(points)} valores únicos")
    for i in points:
        print(i)

def prueba_consulta():
    sensor = 'agsex_sdf_huerto_lht65n_humedad'
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    respuesta = client.query(
        f'SELECT "value" FROM "%" '
        f'WHERE "entity_id" = \'{sensor}\' '
        f'AND time > now() - 2h'
    )
    points = list(respuesta.get_points())
    print(list(points[0].keys()))
    for i in points:
        print(list(i.values()))

def diario_huerto_humedad():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    sensor = 'agsex_sdf_huerto_lht65n_humedad'

    query = (
        'SELECT MEAN("value") AS mean, MIN("value") AS min, MAX("value") AS max '
        'FROM "value" '
        f'WHERE "entity_id" = \'{sensor}\' '
        'AND time > now() - 2d '
        'GROUP BY time(1d)'
    )

    respuesta = client.query(query)
    points = list(respuesta.get_points())

    if not points:
        return None
    else:
        return {
            "mean": points[1]["mean"],
            "min": points[1]["min"],
            "max": points[1]["max"]
        }


def diario_huerto_temperatura():
    client = InfluxDBClient(HOST, PORT, USER, PASS, DB)
    sensor = 'agsex_sdf_huerto_lht65n_temperatura'

    query = (
        'SELECT MEAN("value") AS mean, MIN("value") AS min, MAX("value") AS max '
        'FROM "value" '
        f'WHERE "entity_id" = \'{sensor}\' '
        'AND time > now() - 2d '
        'GROUP BY time(1d)'
    )

    respuesta = client.query(query)
    points = list(respuesta.get_points())

    if not points:
        return None
    else:
        return {
            "mean": points[1]["mean"],
            "min": points[1]["min"],
            "max": points[1]["max"]
        }


if __name__ == '__main__':
    # ping()
    # consulta_bbdd()
    consultar_tablas()
    # consultar_tag_key()
    # consultar_tag_values()
    # consultar_fields()
    # prueba_consulta()
    # diario_huerto_humedad()
    # diario_huerto_temperatura()