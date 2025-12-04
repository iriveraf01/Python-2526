# Ejercicio 2
# Tienes una lista de pedidos de clientes, donde cada pedido es una tupla (cantidad,
# precio_unitario, estado).
# - Filtrar (filter): Obtén solo los pedidos que están en estado 'ENVIADO'.
# - Mapear (map): Calcula el coste total de cada pedido restante (cantidad ×
# precio_unitario).
# - Reducir (reduce): Suma todos los costes totales para obtener el ingreso bruto total de
# los pedidos enviados.
pedidos = [
    (5, 10.0, 'ENVIADO'),
    (10, 2.5, 'PENDIENTE'),
    (2, 50.0, 'ENVIADO'),
    (3, 30.0, 'CANCELADO'),
    (1, 15.0, 'ENVIADO')
]
enviados = list(filter(lambda e: e[2] == "ENVIADO", pedidos))
print(f"Filter---ENVIADOS")
for i in enviados:
    print(f"Pedido: {i}")

coste_total_por_producto = list(map(lambda e: (e[0] * e[1]), enviados))
print("\nMap---COSTE TOTAL")
for i in coste_total_por_producto:
    print(i)

from functools import reduce
costes_totales = reduce(lambda a, b: a + b, coste_total_por_producto)
print("\nReduce---COSTES TOTALES BRUTO")
print(f"Coste total de todos los pedidos: {costes_totales}")

ingreso_alternativo = sum([p[0] * p[1] for p in pedidos if p[2] == 'ENVIADO'])
print(ingreso_alternativo)