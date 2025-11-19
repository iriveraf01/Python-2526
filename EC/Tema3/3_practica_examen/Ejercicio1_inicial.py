STOCK_INICIAL = {
    "martillo": (15.50, 50),
    "clavo_caja": (5.00, 200),
    "sierra_manual": (35.99, 10),
    "cinta_metrica": (8.25, 75),
}

PEDIDOS = [
    {"producto": "martillo", "cantidad": 5},
    {"producto": "sierra_manual", "cantidad": 12},  # No hay stock
    {"producto": "clavo_caja", "cantidad": 150},
    {"producto": "cinta_metrica", "cantidad": 10},
    {"producto": "llave_inglesa", "cantidad": 3}   # Producto no listado
]

# Ejercicio 1
# Estás gestionando el inventario y los pedidos de una ferretería.
# Tenemos un stock inicial que es un diccionario donde la clave es el nombre del
# producto y el valor es una tupla (precio_unitario, cantidad_en_stock).
# Tenemos una lista de pedidos pendientes, donde cada pedido es un diccionario con
# las claves producto y cantidad.
# Crea la función procesar_pedidos(stock, pedidos) que:
# - Recorre la lista de pedidos.
# - Para cada pedido, verifica si hay suficiente stock.
# - Si hay stock, actualiza el diccionario stock restando la cantidad. Calcula el
# costo del pedido.
# - Si no hay stock, registra el nombre del producto en una lista de faltantes.
# - Devuelve una tupla (stock_actualizado, costo_total_pedidos,
# productos_faltantes).
def procesar_pedidos(stock: dict, pedidos: list) -> tuple:
    productos_faltantes = []
    costo_total_pedidos = 0.0
    for pedido in pedidos:
        producto = pedido["producto"]
        cantidad_pedida = pedido["cantidad"]
        
        if producto not in stock:
            productos_faltantes.append(producto)
        else:
            precio_unitario, cantidad_stock = stock[producto]

            if cantidad_pedida > cantidad_stock:
                productos_faltantes.append(producto)
            else:
                costo_total_pedidos += precio_unitario * cantidad_pedida
                stock[producto] = (precio_unitario, cantidad_stock - cantidad_pedida)

    return (stock, costo_total_pedidos, productos_faltantes)

# Prueba
stock_final, costo_final, faltantes = procesar_pedidos(STOCK_INICIAL, PEDIDOS)

print("\n--- EJERCICIO: GESTIÓN DE STOCK ---")
print(f"Costo Total de Pedidos Procesados: {costo_final}€")
print(f"Productos Faltantes/No Existentes: {faltantes}")
print(f"Stock Final de Sierras: {stock_final['sierra_manual']}") # 10 (no se restó)