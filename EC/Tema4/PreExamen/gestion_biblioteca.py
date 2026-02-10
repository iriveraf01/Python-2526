from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, fecha_publicacion: datetime) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.fecha_publicacion = fecha_publicacion

    def es_prestable(self) -> bool:
        fecha_actual = datetime.now()
        meses_diferencia = (fecha_actual.year - self.fecha_publicacion.year) * 12 + (fecha_actual.month - self.fecha_publicacion.month)
        return meses_diferencia > 6

    def __str__(self) -> str:
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"

class Prestamo:
    DIAS_PRESTAMO = 15

    def __init__(self, libro: Libro, usuario: str, fecha_prestamo: datetime = None) -> None:
        if not libro.es_prestable():
            raise ValueError(f"El libro '{libro.titulo}' no es prestable.")
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo if fecha_prestamo else datetime.now()
        self.fecha_devolucion_limite = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        self.fecha_devolucion_real = None

    def calcular_dias_retraso(self, fecha_devolucion: datetime = None) -> int:
        fecha_devolucion = fecha_devolucion if fecha_devolucion else datetime.now()
        if fecha_devolucion <= self.fecha_devolucion_limite:
            return 0
        return (fecha_devolucion - self.fecha_devolucion_limite).days
    
    def devolver_libro(self, fecha_devolucion: datetime = None) -> dict:
        fecha_devolucion = fecha_devolucion if fecha_devolucion else datetime.now()
        self.fecha_devolucion_real = fecha_devolucion
        dias_retraso = self.calcular_dias_retraso(fecha_devolucion)
        multa = dias_retraso * 0.50
        return {
            'libro': self.libro.titulo,
            'usuario': self.usuario,
            'fecha_devolucion': fecha_devolucion,
            'dias_retraso': dias_retraso,
            'multa': multa
        }
    def __str__(self) -> str:
        estado = "Devuelto" if self.fecha_devolucion_real else "Activo"
        fecha_limite_str = self.fecha_devolucion_limite.strftime("%d/%m/%Y")
        return f"Préstamo [{estado}] - '{self.libro.titulo}' por {self.libro.autor} (ISBN: {self.libro.isbn}) - Usuario: {self.usuario} - Fecha límite: {fecha_limite_str}"

class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.prestamos_activos = []
        self.historial_prestamos = []

    def realizar_prestamo(self, libro: Libro, usuario: str) -> bool:
        try:
            nuevo_prestamo = Prestamo(libro, usuario)
            self.prestamos_activos.append(nuevo_prestamo)
            self.historial_prestamos.append(nuevo_prestamo)
            print(f"Préstamo realizado con éxito. Fecha límite de devolución: {nuevo_prestamo.fecha_devolucion_limite.strftime('%d/%m/%Y')}")
            return True
        except ValueError as e:
            print(f"Error al realizar el préstamo: {e}")
            return False

    def devolver_libro(self, isbn: str, fecha_devolucion: datetime = None) -> dict:
        for prestamo in self.prestamos_activos:
            if prestamo.libro.isbn == isbn:
                info_devolucion = prestamo.devolver_libro(fecha_devolucion)
                self.prestamos_activos.remove(prestamo)
                return info_devolucion
        print(f"No se encontró un préstamo activo con ISBN: {isbn}")
        return None
    
    def listar_prestamos_activos(self) -> None:
        if not self.prestamos_activos:
            print("No hay préstamos activos.")
            return
        print(f"Préstamos activos en {self.nombre}:")
        for prestamo in self.prestamos_activos:
            print(prestamo)
            dias_retraso = prestamo.calcular_dias_retraso()
            if dias_retraso > 0:
                multa_acumulada = dias_retraso * 0.50
                print(f"  ¡Advertencia! Retraso de {dias_retraso} días. Multa acumulada: {multa_acumulada:.2f} euros.")

    def generar_estadisticas(self) -> dict:
        total_prestamos = len(self.historial_prestamos)
        prestamos_activos = len(self.prestamos_activos)
        prestamos_completados = total_prestamos - prestamos_activos
        prestamos_con_retraso = sum(1 for prestamo in self.historial_prestamos if prestamo.fecha_devolucion_real and prestamo.calcular_dias_retraso(prestamo.fecha_devolucion_real) > 0)
        return {
            'total_prestamos': total_prestamos,
            'prestamos_activos': prestamos_activos,
            'prestamos_completados': prestamos_completados,
            'prestamos_con_retraso': prestamos_con_retraso
        }

def main():
    """Función principal de prueba del sistema."""

    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca Municipal Central")

    print(f"\n{'='*80}")
    print(f"SISTEMA DE GESTIÓN - {biblioteca.nombre}")
    print(f"{'='*80}\n")

    # Crear libros con diferentes fechas de publicación
    libro1 = Libro(
    "Clean Code",
    "Robert C. Martin",
    "978-0132350884",
    datetime(2023, 1, 15) # Hace más de 6 meses
    )

    libro2 = Libro(
    "Python Crash Course",
    "Eric Matthes",
    "978-1593279288",
    datetime(2024, 11, 1) # Hace menos de 6 meses
    )

    libro3 = Libro(
    "The Pragmatic Programmer",
    "David Thomas",
    "978-0201616224",
    datetime(2022, 5, 20) # Hace más de 6 meses
    )

    # Intentar realizar préstamos
    print("--- REALIZANDO PRÉSTAMOS ---\n")
    biblioteca.realizar_prestamo(libro1, "Ana García")
    biblioteca.realizar_prestamo(libro2, "Carlos López") # Error: libro muy reciente
    biblioteca.realizar_prestamo(libro3, "María Rodríguez")

    # Listar préstamos activos
    biblioteca.listar_prestamos_activos()

    # Simular devolución a tiempo
    print("\n--- DEVOLUCIÓN A TIEMPO ---")
    fecha_devolucion_a_tiempo = datetime.now() + timedelta(days=10)
    info_dev = biblioteca.devolver_libro("978-0132350884",
    fecha_devolucion_a_tiempo)
    if info_dev:
        print(f"Libro: {info_dev['libro']}")
        print(f"Usuario: {info_dev['usuario']}")
        print(f"Días de retraso: {info_dev['dias_retraso']}")
        print(f"Multa: {info_dev['multa']:.2f}€\n")

    # Simular devolución con retraso
    print("--- DEVOLUCIÓN CON RETRASO ---")
    fecha_devolucion_tarde = datetime.now() + timedelta(days=20)
    info_dev = biblioteca.devolver_libro("978-0201616224",
    fecha_devolucion_tarde)
    if info_dev:
        print(f"Libro: {info_dev['libro']}")
        print(f"Usuario: {info_dev['usuario']}")
        print(f"Días de retraso: {info_dev['dias_retraso']}")
        print(f"Multa: {info_dev['multa']:.2f}€\n")

    # Mostrar estadísticas
    print("--- ESTADÍSTICAS DE LA BIBLIOTECA ---")
    stats = biblioteca.generar_estadisticas()
    print(f"Total de préstamos realizados: {stats['total_prestamos']}")
    print(f"Préstamos activos: {stats['prestamos_activos']}")
    print(f"Préstamos completados: {stats['prestamos_completados']}")
    print(f"Préstamos con retraso: {stats['prestamos_con_retraso']}")
    print(f"\n{'='*80}\n")

if __name__ == "__main__":
    main()