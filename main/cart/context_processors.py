from cart.models import Cart

def user_carts(request):
  if request.user.is_authenticated:
    return {'carts': Cart.objects.filter(user=request.user)}
  
  if not request.session.session_key:
    request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')