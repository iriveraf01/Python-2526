# Crear una clase Producto con las especificaciones:
# - Atributos privados: nombre, codigo_lote
# - Atributos de clase: diccionario STOCK_TOTAL donde la clave es el nombre del
# producto y el valor es la cantidad de unidades en stock.
# - El atributo codigo_lote debe tener 8 caracteres y comenzar por la letra “L”, si no
# cumple, lanzar la excepción ValueError.
# - El atributo nombre debe ser inmutable, es decir, que no se va a poder cambiar una
# vez creado el objeto.
# - Al crear el objeto se debe incrementar STOCK_TOTAL(una vez validado que el lote es
# correcto). Mostrar el mensaje “Producto X (Lote:X) creado y añadido al stock”.
# - Crear un método de instancia vender() que reduzca la cantidad del producto en 1
# unidad, si el stock es 0 antes de la venta, lanzar la excepción RuntimeError y no debe
# permitir la venta. Mostrar el mensaje si se ha podido realizar la venta correctamente:
# “Venta de X realizada. Stock restante: X”.
class Producto:
    STOCK_TOTAL = {}
    def __init__(self, nombre, codigo_lote):
    
        self.__nombre = nombre
        self.codigo_lote = codigo_lote
    
        if nombre in Producto.STOCK_TOTAL:
            Producto.STOCK_TOTAL[nombre] += 1
            print(f"Producto {self.nombre} (Lote:{self.codigo_lote}) stock incrementado a {self.STOCK_TOTAL[self.nombre]}.")
        else:
            Producto.STOCK_TOTAL[nombre] = 1
            print(f"Producto {self.nombre} (Lote:{self.codigo_lote}) creado y añadido al stock.")

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def codigo_lote(self):
        return self.__codigo_lote
    @codigo_lote.setter
    def codigo_lote(self, valor):
        if len(valor) != 8 or not valor.startswith("L"):
            raise ValueError("El código de lote debe tener 8 caracteres y comenzar por 'L'.")
        self.__codigo_lote = valor.upper()

    def vender(self):
        if Producto.STOCK_TOTAL[self.nombre] == 0:
            raise RuntimeError("Stock agotado. No se puede realizar la venta.")
        Producto.STOCK_TOTAL[self.nombre] -= 1
        print(f"Venta de {self.nombre} realizada. Stock restante: {Producto.STOCK_TOTAL[self.nombre]}")

# Crea una clase estática llamada Trazabilidad que tendrá:
# - Método estático llamado consultar_stock_total(), que recibirá el diccionario de
# Producto.STOCK_TOTAL e imprimir un listado de los productos(ordenado por nombre
# de producto), mostrando el stock disponible.
# - Añadir un método a la clase Trazabilidad para que genere un reporte de bajo stock,
# este método se llamará generar_reporte_bajo_stock y tendrá como parámetros de
# entrada el inventario y el umbral a partir del cual se considera stock bajo. Si todos los
# productos están por encima del umbral mostrar: “Todos los productos están por
# encima del umbral” en caso contrario mostrar: “
# - Añade un método a la clase Trazabilidad llamado listar_nombres_disponibles que
# tendrá el inventario como parámetro de entrada donde se use list comprehesion para
# mostrar solo los nombres de los productos en stock separados por coma (,).
class Trazabilidad:
    @staticmethod
    def consultar_stock_total(Producto_STOCK_TOTAL):
        print("\n--- Stock Total de Productos ---")
        for nombre in sorted(Producto_STOCK_TOTAL.keys()):
            print(f"Producto: {nombre}, Stock Disponible: {Producto_STOCK_TOTAL[nombre]}")
        print("--------------------------------\n")
    
    @staticmethod
    def generar_reporte_bajo_stock(stock_total, umbral):
        productos_bajos = [(nombre, stock) for nombre, stock in stock_total.items() if stock <= umbral]
        if not productos_bajos:
            print("Todos los productos están por encima del umbral.")
            return
        
        print(f"Hay {len(productos_bajos)} por debajo del umbral:")

        for nombre, stock in productos_bajos:
            print(f"- {nombre}: {stock}")

    @staticmethod
    def listar_nombres_disponibles(stock_total):
        nombres = [nombre for nombre, stock in stock_total.items() if stock > 0]
        print("Nombres de productos en stock: " + ", ".join(sorted(nombres)))
# --- ZONA DE PRUEBA ---

print("### INICIO DE LA GESTIÓN DE LOTES ###")

# 1. Creación y validación exitosa
try:
    p1 = Producto("Paracetamol", "LOTE-P45") # Lote válido
    p2 = Producto("Amoxicilina", "LOTE-A10") # Lote válido
    p3 = Producto("Paracetamol", "LOTE-X99") # Lote válido, incrementa stock
except ValueError as e:
    print(f"Error al crear producto válido: {e}")

Trazabilidad.consultar_stock_total(Producto.STOCK_TOTAL)

# 2. Intento de creación con lote inválido (Debe fallar)
try:
    p_invalido_long = Producto("Vitamina C", "LOTE") # Longitud incorrecta
except ValueError as e:
    print(f"\nExcepción esperada (Longitud): {e}")

try:
    p_invalido_prefijo = Producto("Aspirina", "XOTE-A22") # Prefijo incorrecto
except ValueError as e:
    print(f"\nExcepción esperada (Prefijo): {e}")


# 3. Simulación de ventas
print("\n--- Simulación de Ventas ---")
p1.vender() # Vender Paracetamol (Stock 2 -> 1)
p1.vender() # Vender Paracetamol (Stock 1 -> 0)

# 4. Intento de venta de stock agotado (Debe fallar)
try:
    p1.vender() # Vender Paracetamol (Stock 0 -> Error)
except RuntimeError as e:
    print(f"\nExcepción esperada (Stock agotado): {e}")
    
Trazabilidad.consultar_stock_total(Producto.STOCK_TOTAL)

Trazabilidad.generar_reporte_bajo_stock(Producto.STOCK_TOTAL, 1)
print("--------------------------------")
Trazabilidad.listar_nombres_disponibles(Producto.STOCK_TOTAL)
print("--------------------------------")