from datetime import datetime, timedelta

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int, fecha_creacion=None) -> None:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
    
    def agregar_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.stock += cantidad
    
    def reducir_stock(self, cantidad: int) -> bool:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True
    
    def calcular_valor_inventario(self) -> float:
        return self.stock * self.precio
    
    def to_dict(self) -> dict:
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio': self.precio,
            'stock': self.stock,
            'fecha_creacion': self.fecha_creacion.isoformat()
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Producto':
        fecha_creacion = datetime.fromisoformat(data['fecha_creacion'])
        return Producto(
            codigo=data['codigo'],
            nombre=data['nombre'],
            categoria=data['categoria'],
            precio=data['precio'],
            stock=data['stock'],
            fecha_creacion=fecha_creacion
        )
    
    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.categoria} | Precio: {self.precio:.2f}€ | Stock: {self.stock} unidades"
    
class MovimientoInventario:
    def __init__(self, producto_codigo: str, tipo: str, cantidad: int, observaciones: str = "", fecha: datetime = None) -> None:
        if tipo not in ["ENTRADA", "SALIDA"]:
            raise ValueError("El tipo debe ser 'ENTRADA' o 'SALIDA'")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        self.producto_codigo = producto_codigo
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha if fecha else datetime.now()
        self.observaciones = observaciones
    
    def to_dict(self) -> dict:
        return {
            'producto_codigo': self.producto_codigo,
            'tipo': self.tipo,
            'cantidad': self.cantidad,
            'fecha': self.fecha.isoformat(),
            'observaciones': self.observaciones
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'MovimientoInventario':
        fecha = datetime.fromisoformat(data['fecha'])
        return MovimientoInventario(
            producto_codigo=data['producto_codigo'],
            tipo=data['tipo'],
            cantidad=data['cantidad'],
            observaciones=data['observaciones'],
            fecha=fecha
        )
    
    def __str__(self) -> str:
        fecha_str = self.fecha.strftime("%d/%m/%Y %H:%M")
        return f"[{fecha_str}] {self.tipo} - {self.producto_codigo} - {self.cantidad} unidades - {self.observaciones}"

class Inventario:
    def __init__(self, archivo_productos: str = "productos.json", archivo_movimientos: str = "movimientos.json") -> None:
        self.productos = {}
        self.movimientos = []
        self.archivo_productos = archivo_productos
        self.archivo_movimientos = archivo_movimientos

    def agregar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self.productos:
            print(f"Error: El producto con código '{producto.codigo}' ya existe.")
            return False
        self.productos[producto.codigo] = producto
        print(f"Producto '{producto.nombre}' agregado exitosamente.")
        return True
    
    def buscar_producto(self, codigo: str) -> Producto:
        return self.productos.get(codigo)
    
    def registrar_entrada(self, codigo: str, cantidad: int, observaciones: str = "") -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            print(f"Error: Producto con código '{codigo}' no encontrado.")
            return False
        try:
            producto.agregar_stock(cantidad)
            movimiento = MovimientoInventario(codigo, "ENTRADA", cantidad, observaciones)
            self.movimientos.append(movimiento)
            print(f"Entrada registrada: {cantidad} unidades de '{producto.nombre}'.")
            return True
        except ValueError as e:
            print(f"Error al registrar entrada: {e}")
            return False
        
    def registrar_salida(self, codigo: str, cantidad: int, observaciones: str = "") -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            print(f"Error: Producto con código '{codigo}' no encontrado.")
            return False
        try:
            if not producto.reducir_stock(cantidad):
                print(f"Stock insuficiente para el producto '{producto.nombre}'.")
                return False
            movimiento = MovimientoInventario(codigo, "SALIDA", cantidad, observaciones)
            self.movimientos.append(movimiento)
            print(f"Salida registrada: {cantidad} unidades de '{producto.nombre}'.")
            return True
        except ValueError as e:
            print(f"Error al registrar salida: {e}")
            return False
        
    def listar_productos(self, categoria: str = None) -> None:
        productos_filtrados = self.productos.values()
        if categoria:
            productos_filtrados = filter(lambda p: p.categoria == categoria, productos_filtrados)
        
        productos_filtrados = list(productos_filtrados)
        
        if not productos_filtrados:
            print("No hay productos en el inventario.")
            return
        
        print(f"{'Código':<10} {'Nombre':<30} {'Categoría':<15} {'Precio':<10} {'Stock':<10} {'Valor Total':<15}")
        print("-" * 90)
        valor_total_inventario = 0
        for producto in productos_filtrados:
            valor_inventario = producto.calcular_valor_inventario()
            valor_total_inventario += valor_inventario
            print(f"{producto.codigo:<10} {producto.nombre:<30} {producto.categoria:<15} {producto.precio:<10.2f} {producto.stock:<10} {valor_inventario:<15.2f}")
        print("-" * 90)
        print(f"Valor total del inventario: {valor_total_inventario:.2f}€")

    def listar_movimientos(self, codigo_producto: str = None, limite: int = 10) -> None:
        movimientos_filtrados = self.movimientos
        if codigo_producto:
            movimientos_filtrados = filter(lambda m: m.producto_codigo == codigo_producto, movimientos_filtrados)
        
        movimientos_filtrados = sorted(movimientos_filtrados, key=lambda m: m.fecha, reverse=True)[:limite]
        
        if not movimientos_filtrados:
            print("No hay movimientos registrados.")
            return
        
        for movimiento in movimientos_filtrados:
            print(movimiento)

    def guardar_datos(self) -> bool:
        import json
        try:
            with open(self.archivo_productos, 'w', encoding='utf-8') as f_prod:
                json.dump([p.to_dict() for p in self.productos.values()], f_prod, indent=4, ensure_ascii=False)
            with open(self.archivo_movimientos, 'w', encoding='utf-8') as f_mov:
                json.dump([m.to_dict() for m in self.movimientos], f_mov, indent=4, ensure_ascii=False)
            print("Datos guardados exitosamente.")
            return True
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False
        
    def cargar_datos(self) -> bool:
        import json
        import os
        if not os.path.exists(self.archivo_productos) or not os.path.exists(self.archivo_movimientos):
            print("No se encontraron archivos de datos. Se iniciará con un inventario vacío.")
            return False
        try:
            with open(self.archivo_productos, 'r', encoding='utf-8') as f_prod:
                productos_data = json.load(f_prod)
                for prod_dict in productos_data:
                    producto = Producto.from_dict(prod_dict)
                    self.productos[producto.codigo] = producto
            with open(self.archivo_movimientos, 'r', encoding='utf-8') as f_mov:
                movimientos_data = json.load(f_mov)
                for mov_dict in movimientos_data:
                    movimiento = MovimientoInventario.from_dict(mov_dict)
                    self.movimientos.append(movimiento)
            print("Datos cargados exitosamente.")
            return True
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return False
        
    def generar_informe_categoria(self) -> dict:
        informe = {}
        for producto in self.productos.values():
            cat = producto.categoria
            if cat not in informe:
                informe[cat] = {'productos': 0, 'stock_total': 0, 'valor_total': 0.0}
            informe[cat]['productos'] += 1
            informe[cat]['stock_total'] += producto.stock
            informe[cat]['valor_total'] += producto.calcular_valor_inventario()
        return informe

def main():
    """Función principal de prueba del sistema."""
    
    print(f"\n{'='*90}")
    print("SISTEMA DE GESTIÓN DE INVENTARIO")
    print(f"{'='*90}\n")
    
    # Crear inventario
    inventario = Inventario()
    
    # Intentar cargar datos existentes
    print("Cargando datos existentes...")
    inventario.cargar_datos()
    
    print("\n--- AGREGANDO PRODUCTOS ---")
    
    # Crear productos
    try:
        prod1 = Producto("PROD001", "Laptop Dell", "Electrónica", 899.99, 0)
        inventario.agregar_producto(prod1)
        
        prod2 = Producto("PROD002", "Mouse Logitech", "Electrónica", 29.99, 0)
        inventario.agregar_producto(prod2)
        
        prod3 = Producto("PROD003", "Arroz Integral", "Alimentación", 3.50, 200)
        inventario.agregar_producto(prod3)
        
        prod4 = Producto("PROD004", "Aceite de Oliva", "Alimentación", 12.99, 50)
        inventario.agregar_producto(prod4)
        
        # Intentar agregar producto duplicado
        prod_duplicado = Producto("PROD001", "Otro Producto", "Otra", 100.0, 10)
        inventario.agregar_producto(prod_duplicado)
        
    except ValueError as e:
        print(f"✗ Error al crear producto: {e}")
    
    print("\n--- REGISTRANDO ENTRADAS ---")
    
    # Registrar entradas
    inventario.registrar_entrada("PROD001", 50, "Compra proveedor")
    inventario.registrar_entrada("PROD002", 100, "Reposición")
    inventario.registrar_entrada("PROD003", 150, "Compra mayorista")
    
    # Intentar entrada con cantidad negativa
    inventario.registrar_entrada("PROD001", -10, "Intento inválido")
    
    print("\n--- REGISTRANDO SALIDAS ---")
    
    # Registrar salidas
    inventario.registrar_salida("PROD001", 5, "Venta cliente")
    inventario.registrar_salida("PROD002", 10, "Venta online")
    inventario.registrar_salida("PROD003", 50, "Distribución tienda")
    
    # Intentar salida que supera el stock
    inventario.registrar_salida("PROD002", 200, "Pedido grande")
    
    # Intentar salida de producto inexistente
    inventario.registrar_salida("PROD999", 10, "Producto fantasma")
    
    print("\n--- LISTADO COMPLETO DE PRODUCTOS ---")
    inventario.listar_productos()
    
    print("--- PRODUCTOS POR CATEGORÍA: ELECTRÓNICA ---")
    inventario.listar_productos("Electrónica")
    
    print("--- PRODUCTOS POR CATEGORÍA: ALIMENTACIÓN ---")
    inventario.listar_productos("Alimentación")
    
    # Listar movimientos
    inventario.listar_movimientos()
    
    print("--- MOVIMIENTOS DEL PRODUCTO PROD001 ---")
    inventario.listar_movimientos("PROD001", limite=5)
    
    print("\n--- INFORME POR CATEGORÍAS ---")
    informe = inventario.generar_informe_categoria()
    
    for categoria, datos in informe.items():
        print(f"\nCategoría: {categoria}")
        print(f"  Productos: {datos['productos']}")
        print(f"  Stock total: {datos['stock_total']} unidades")
        print(f"  Valor total: {datos['valor_total']:,.2f}€")
    
    print("\n--- GUARDANDO DATOS ---")
    inventario.guardar_datos()
    
    print("\n--- DEMOSTRACIÓN DE CARGA DE DATOS ---")
    print("Creando nuevo inventario y cargando datos guardados...")
    
    nuevo_inventario = Inventario()
    nuevo_inventario.cargar_datos()
    
    print("\nProductos en el nuevo inventario:")
    nuevo_inventario.listar_productos()
    
    print(f"\n{'='*90}\n")

if __name__ == "__main__":
    main()