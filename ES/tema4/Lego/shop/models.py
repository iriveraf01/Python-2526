from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 1. PERFIL DE USUARIO
class Profile(models.Model):
    # Relación OneToOne: Un usuario tiene un perfil, un perfil pertenece a un usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    es_vendedor = models.BooleanField(default=False)
    solicita_vendedor = models.BooleanField(default=False, verbose_name="Solicita ser vendedor")
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# 2. CATEGORÍA
class Category(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nombre

# 3. PRODUCTO
class Product(models.Model):
    # Definimos las opciones para el campo estado
    ESTADO_CHOICES = [
        ('NUEVO', 'Nuevo / Sellado'),
        ('COMPLETO', 'Abierto / Completo'),
        ('INCOMPLETO', 'Incompleto'),
        ('PIEZAS', 'Solo piezas'),
    ]

    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)
    estado = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default='NUEVO'
    )
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    

from django.db.models.signals import post_save
from django.dispatch import receiver

# Esta función se ejecuta cada vez que se guarda un User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Si el usuario se acaba de crear, le creamos su perfil
        Profile.objects.create(user=instance)

# Esta función asegura que si se actualiza el User, se guarde el perfil
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# 4. PEDIDO (ORDER)
class Order(models.Model):
    ESTADO_CHOICES = [
        ('PREPARACION', 'En preparación'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGADO', 'Entregado'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PREPARACION')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.user.username}"

# 5. DETALLE DE PEDIDO (ORDER ITEM)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.product.nombre}"