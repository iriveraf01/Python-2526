def cart_counter(request):
    """Hace disponible el número de ítems del carrito en todos los templates."""
    cart = request.session.get('cart', {})
    count = sum(cart.values())
    return {'cart_count': count}
