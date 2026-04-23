from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('registro/', view=views.registro, name='registro'),
    path('logout/', view=views.cerrar_sesion, name='logout'),
    path('login/', view=views.iniciar_sesion, name='login'),
    path('perfil/', view=views.perfil, name='perfil'),
    path('catalogo/', view=views.catalogo, name='catalogo'),
    path('carrito/add/<int:product_id>/', view=views.add_to_cart, name='add_to_cart'),
    path('carrito/', view=views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<int:product_id>/', view=views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('checkout/', view=views.checkout, name='checkout'),
    path('vender/subir/', view=views.subir_producto, name='subir_producto'),
    path('vender/mis-productos/', view=views.mis_productos, name='mis_productos'),
    path('vender/marcar-enviado/<int:order_id>/', view=views.marcar_enviado, name='marcar_enviado'),
]
