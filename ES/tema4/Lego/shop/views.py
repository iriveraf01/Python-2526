from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, UserUpdateForm, ProfileUpdateForm, ProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from .models import Product, Category

# Create your views here.
# Vista de la página de inicio de la tienda
def index(request):
    return render(request, 'shop/index.html')

def registro(request):
    if request.method == 'POST':
        # Aquí procesaríamos el formulario de registro
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'shop/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def iniciar_sesion(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Usuario o contraseña incorrectos. Revisa tus piezas."
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form, 'error_messages': error_message})

from .models import Product, Category, Order, OrderItem
from django.db import transaction

@login_required
def perfil(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    # Obtenemos el historial de pedidos del usuario
    pedidos = request.user.pedidos.all().order_by('-fecha')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'pedidos': pedidos
    }
    return render(request, 'shop/perfil.html', context)

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('catalogo')

def ver_carrito(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, cantidad in cart.items():
        producto = Product.objects.get(id=product_id)
        subtotal = producto.precio * cantidad
        total += subtotal
        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
    return render(request, 'shop/carrito.html', {'items': items, 'total': total})

def eliminar_del_carrito(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('ver_carrito')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('catalogo')
    
    items = []
    total = 0
    for product_id, cantidad in cart.items():
        producto = Product.objects.get(id=product_id)
        total += producto.precio * cantidad
        items.append({'producto': producto, 'cantidad': cantidad})

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        with transaction.atomic():
            pedido = Order.objects.create(
                user=request.user,
                direccion_entrega=direccion,
                total=total
            )
            for item in items:
                OrderItem.objects.create(
                    order=pedido,
                    product=item['producto'],
                    cantidad=item['cantidad'],
                    precio_unitario=item['producto'].precio
                )
            # Limpiar carrito
            request.session['cart'] = {}
            return render(request, 'shop/pedido_confirmado.html', {'pedido': pedido})

    return render(request, 'shop/checkout.html', {'items': items, 'total': total})

def catalogo(request):
    productos = Product.objects.all()
    categorias = Category.objects.all()

    # Filtros
    cat_id = request.GET.get('categoria')
    estado = request.GET.get('estado')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    orden = request.GET.get('orden')

    if cat_id:
        productos = productos.filter(categoria_id=cat_id)
    if estado:
        productos = productos.filter(estado=estado)
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    if orden == 'asc':
        productos = productos.order_by('precio')
    elif orden == 'desc':
        productos = productos.order_by('-precio')
    else:
        productos = productos.order_by('-id')

    # Paginación (6 por página)
    paginator = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categorias': categorias,
        'estados': Product.ESTADO_CHOICES,
        'current_cat': cat_id,
        'current_estado': estado,
        'current_pmin': precio_min,
        'current_pmax': precio_max,
        'current_orden': orden,
    }
    return render(request, 'shop/catalogo.html', context)

@login_required
def subir_producto(request):
    if not request.user.profile.es_vendedor:
        return redirect('index')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user

            # Si se escribe una nueva categoría, crearla o reutilizarla
            nueva_cat_nombre = form.cleaned_data.get('nueva_categoria', '').strip()
            if nueva_cat_nombre:
                categoria, _ = Category.objects.get_or_create(nombre=nueva_cat_nombre)
                producto.categoria = categoria
            elif not producto.categoria:
                form.add_error('categoria', 'Selecciona una categoría existente o crea una nueva.')
                return render(request, 'shop/subir_producto.html', {'form': form})

            producto.save()

            # Si no se subió archivo pero sí hay URL, descargar la imagen
            if not producto.imagen and form.cleaned_data.get('imagen_url'):
                import urllib.request
                from django.core.files.base import ContentFile
                img_url = form.cleaned_data['imagen_url']
                try:
                    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        filename = img_url.split('/')[-1]
                        if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                            filename = f"producto_{producto.id}.jpg"
                        producto.imagen.save(filename, ContentFile(response.read()), save=True)
                except Exception:
                    pass  # Si falla la URL, simplemente quedará sin imagen

            return redirect('mis_productos')
    else:
        form = ProductForm()
    return render(request, 'shop/subir_producto.html', {'form': form})

@login_required
def mis_productos(request):
    if not request.user.profile.es_vendedor:
        return redirect('index')
    
    from .models import OrderItem
    # IDs de productos del vendedor que han sido comprados
    vendidos_ids = OrderItem.objects.filter(
        product__vendedor=request.user
    ).values_list('product_id', flat=True)
    
    en_venta = Product.objects.filter(vendedor=request.user).exclude(id__in=vendidos_ids)
    
    # Para cada producto vendido, obtenemos el OrderItem con info del comprador
    vendidos = OrderItem.objects.filter(product__vendedor=request.user).select_related('order__user', 'product')
    
    return render(request, 'shop/mis_productos.html', {
        'en_venta': en_venta,
        'vendidos': vendidos,
    })

@login_required
def marcar_enviado(request, order_id):
    from .models import Order, OrderItem
    order = Order.objects.get(id=order_id)
    # Verificar que el pedido contiene al menos un producto de este vendedor
    if OrderItem.objects.filter(order=order, product__vendedor=request.user).exists():
        order.estado = 'ENVIADO'
        order.save()
    return redirect('mis_productos')