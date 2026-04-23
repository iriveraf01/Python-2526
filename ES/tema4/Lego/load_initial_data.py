import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legocollect.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Category, Product
from django.core.files.base import ContentFile
import urllib.request

def populate():
    print("=== Iniciando carga de datos ===")
    
    # 1. Crear Vendedor
    vendedor, created = User.objects.get_or_create(username='vendedor_test', email='vendedor@test.com')
    if created:
        vendedor.set_password('123456')
        vendedor.save()
        # El signal create_user_profile crea el perfil automáticamente
        vendedor.profile.es_vendedor = True
        vendedor.profile.save()
        print("-> Usuario 'vendedor_test' (password: 123456) creado y configurado como vendedor.")
    else:
        print("-> Usuario 'vendedor_test' ya existe.")

    # 2. Crear Categorías
    categorias_data = [
        ('Star Wars', 'Sets inspirados en la saga galáctica. Naves, dioramas y más.'),
        ('City', 'Vehículos, edificios y situaciones de la vida en la ciudad.'),
        ('Technic', 'Modelos avanzados con funciones mecánicas realistas.'),
        ('Creator Expert', 'Modelos detallados y desafiantes para constructores expertos.')
    ]
    
    categorias = {}
    for nombre, desc in categorias_data:
        cat, c_created = Category.objects.get_or_create(nombre=nombre, defaults={'descripcion': desc})
        categorias[nombre] = cat
        if c_created:
            print(f"-> Categoría '{nombre}' creada.")

    # 3. Crear Productos
    productos_data = [
        {
            'nombre': 'Halcón Milenario UCS',
            'descripcion': 'El modelo Ultimate Collector Series definitivo con más de 7500 piezas.',
            'precio': 799.99,
            'cantidad': 1,
            'estado': 'NUEVO',
            'categoria': categorias['Star Wars'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/75192-1.jpg'
        },
        {
            'nombre': 'Comisaría de Policía',
            'descripcion': 'Estación de policía clásica, falta el helicóptero.',
            'precio': 45.50,
            'cantidad': 1,
            'estado': 'INCOMPLETO',
            'categoria': categorias['City'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/60316-1.jpg'
        },
        {
            'nombre': 'Bugatti Chiron',
            'descripcion': 'Réplica Technic a escala 1:8 con motor W16 móvil.',
            'precio': 350.00,
            'cantidad': 2,
            'estado': 'COMPLETO',
            'categoria': categorias['Technic'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/42083-1.jpg'
        },
        {
            'nombre': 'Caza Estelar X-Wing',
            'descripcion': 'Nave de Luke Skywalker. Solo se venden las piezas sueltas.',
            'precio': 15.00,
            'cantidad': 5,
            'estado': 'PIEZAS',
            'categoria': categorias['Star Wars'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/75301-1.jpg'
        },
        {
            'nombre': 'Tren de Mercancías',
            'descripcion': 'Tren motorizado City con varias vías y vagones.',
            'precio': 180.00,
            'cantidad': 1,
            'estado': 'NUEVO',
            'categoria': categorias['City'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/60198-1.jpg'
        },
        {
            'nombre': 'Máquina de Escribir',
            'descripcion': 'Precioso modelo vintage que funciona de verdad.',
            'precio': 210.00,
            'cantidad': 1,
            'estado': 'COMPLETO',
            'categoria': categorias['Creator Expert'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/21327-1.jpg'
        },
        {
            'nombre': 'Lote piezas surtidas (1kg)',
            'descripcion': 'Caja con un montón de piezas aleatorias limpias.',
            'precio': 25.00,
            'cantidad': 10,
            'estado': 'PIEZAS',
            'categoria': categorias['City'],
            'vendedor': vendedor,
            'img_url': 'https://images.brickset.com/sets/images/10698-1.jpg'
        }
    ]

    for p_data in productos_data:
        # Extraemos la URL de imagen si existe (opcional)
        img_url = p_data.pop('img_url', None)
        
        prod, p_created = Product.objects.get_or_create(
            nombre=p_data['nombre'],
            defaults=p_data
        )
        
        # Intentamos descargar la imagen si el producto es nuevo O si no tiene imagen aún
        if p_created or not prod.imagen:
            if p_created:
                print(f"-> Producto '{prod.nombre}' añadido al catálogo.")
            else:
                print(f"-> El producto '{prod.nombre}' ya existe, pero le falta la imagen. Intentando descargar...")

            if img_url:
                try:
                    print(f"   Descargando imagen para {prod.nombre}...")
                    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        # Usamos el nombre original del archivo de la URL si es posible
                        filename = img_url.split('/')[-1]
                        if not filename.endswith(('.jpg', '.jpeg', '.png')):
                            filename = f"producto_{prod.id}.jpg"
                        
                        # Guardamos directamente usando ContentFile
                        prod.imagen.save(filename, ContentFile(response.read()), save=True)
                        print(f"   Imagen guardada correctamente.")
                except Exception as e:
                    print(f"   No se pudo cargar la imagen: {e}")
        else:
            print(f"-> Producto '{prod.nombre}' ya tiene imagen.")

    print("=== Carga completada ===")

if __name__ == '__main__':
    populate()
