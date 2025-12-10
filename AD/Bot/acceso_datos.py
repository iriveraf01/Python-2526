from influxdb import InfluxDBClient
import pandas as pd

HOST = '10.0.0.8'
PUERTO = 8886
USER = 'pythonread'
PASS = 'read1234'
DATABASE = 'agro_sensex'


def ping():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    print("Prueba de conexión")
    ping_result = client.ping()

    if ping_result:
        print(ping_result)
    else:
        print("No conectado")

def consulta_bbdd():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    print("Mostrando bases de datos...\n")
    databases = client.get_list_database()

    for db in databases:
        print(db['name'])

def consultar_tablas():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    client.switch_database(DATABASE)

    print("Mostrando tablas de la base de datos...\n")

    respuesta = client.query('SHOW MEASUREMENTS')
    points = respuesta.get_points()

    for point in points:
        print(point['name'])

def consultar_tag_key():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    client.switch_database(DATABASE)

    print("Mostrando tag keys...\n")

    respuesta = client.query('SHOW TAG KEYS FROM "%"')
    points = list(respuesta.get_points())

    for point in points:
        print(point)

def consultar_tag_values():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    client.switch_database(DATABASE)

    print("Mostrando valores únicos de la columna entity_id...\n")

    respuesta = client.query('SHOW TAG VALUES FROM "%" WITH KEY = "entity_id"')
    points = list(respuesta.get_points())

    for point in points:
        print(point)

def prueba_consulta():
    sensor = "agsex_sdf_huerto_lht65n_humedad"
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    client.switch_database(DATABASE)

    print("Mostrando los datos de las 2 últimas horas del sensor", sensor, "...\n")
    respuesta = client.query(
        f'SELECT "value" FROM "%" '
        f'WHERE "entity_id" = \'{sensor}\''
        f'AND time > now() - 2h'
    )

    points = list(respuesta.get_points())
    print(list(points[0].keys()))

    for point in points:
        print(list(point.values()))


def diario_huerto_humedad():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    client.switch_database(DATABASE)
    sensor = "agsex_sdf_huerto_lht65n_humedad"

    query = (
        f'SELECT MEAN("value"), MIN("value"), MAX("value") FROM "%"'
        f'WHERE "entity_id" = \'{sensor}\''
        f'AND time >= now() - 2d '
        f'GROUP BY time(1d)'
    )

    respuesta = client.query(query)
    points = list(respuesta.get_points())

    if not points:
        return {}
    
    point = points[1]
    datos = dict()

    datos["media"] = round(point['mean'],1)
    datos["minimo"] = round(point['min'],1)
    datos["maximo"] = round(point['max'],1)

    return datos

def diario_huerto_temperatura():
    client = InfluxDBClient(host=HOST, port=PUERTO, username=USER, password=PASS)
    client.switch_database(DATABASE)
    sensor = "agsex_sdf_huerto_lht65n_temperatura"

    query = (
        f'SELECT MEAN("value"), MIN("value"), MAX("value") FROM "°C"'
        f'WHERE "entity_id" = \'{sensor}\''
        f'AND time >= now() - 2d '
        f'GROUP BY time(1d)'
    )

    respuesta = client.query(query)
    points = list(respuesta.get_points())

    if not points:
        return {}
    
    point = points[1]
    datos = dict()

    datos["media"] = round(point['mean'],1)
    datos["minimo"] = round(point['min'],1)
    datos["maximo"] = round(point['max'],1)

    return datos

if __name__ == '__main__':
    print(diario_huerto_temperatura())