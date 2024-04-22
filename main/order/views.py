from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect, render
from cart.models import Cart
from payment.alfabank import create_payment, get_status
from .email_send import email_send
from order.models import Order, OrderItem
from order.forms import CreateOrderForm
from django.contrib.auth.decorators import login_required

def order(request):
  ...

def order_create(request):
  form = CreateOrderForm(request.POST)
  if request.method == "POST":
    """Получаем способ оплаты и в зависимости от метода оплаты строим логику ниже"""
    payment_method = request.POST['payment_option']
    if form.is_valid():
      try:
        order = form.save(commit=False)
        if request.user.is_authenticated:
          user = request.user
          order.user = user
          # Получаем корзину пользователя если он авторизован
        else:
          order.user = None
          # Получаем корзину пользователя если он не авторизован по ключу сессии
          session_key = request.session.session_key
          cart_items = Cart.objects.filter(session_key=session_key)
          
          try: 
            first_name = request.POST['first_name']
            order.first_name = first_name
          except:
            pass
          
          try:
            email = request.POST['email']
            order.email = email
          except:
            pass
          
          try:
            first_name_human = request.POST['first_name_human']
            order.first_name_human = first_name_human
          except:
            pass
          
          try:
            phone_number_human = request.POST['phone_number_human']
            order.phone_number_human = phone_number_human
          except:
            pass
          
          try:
            pickup = request.POST['pickup']
            order.pickup = True
          except:
            pass
          
          try:
            surprise = request.POST['surprise']
            order.surprise = True
          except:
            pass
          
          try:
            anonymous = request.POST['anonymous']
            order.anonymous = True
          except:
            pass
          
          try:
            phone = request.POST['phone']
            order.phone = phone
          except:
            pass
          
          try:
            delivery_address = request.POST['delivery_address']
            order.delivery_address = delivery_address
          except: 
            pass
          
          try:
            pay_method = request.POST['payment_option']
            order.pay_method = pay_method
          except: 
            pass
        
          order.save()
          for item in cart_items:
            product=item.product
            name=item.product.name
            price=item.product.sell_price()
            quantity=item.quantity
            
            orderItem  = OrderItem.objects.create(
              order = order,
              product=product,
              name=name,
              price=price,
              quantity=quantity
            )
          if payment_method == "На сайте картой":
              data = create_payment(orderItem, cart_items, request)
              payment_id = data["id"]
              confirmation_url = data["confirmation_url"]

              order.payment_id = payment_id
              order.payment_dop_info = confirmation_url
              order.save()
              return redirect(confirmation_url)
          else:
            email_send(order)
            cart_items.delete()
            return redirect('order_succes')
      except Exception as e:
        print(e)
  
  # cart = request.context['cart_my']
  
  session_key = request.session.session_key
  cart_items = Cart.objects.filter(session_key=session_key)
  context = {
    'title': 'Home - Оформление заказа',
    'orders': True,
    "cart": cart_items
  }
      
  return render(request, "pages/orders/create.html", context)

def order_error(request):
    return render(request, "pages/orders/error.html")

def order_success(request):
    session_key = request.session.session_key
    cart = Cart.objects.filter(session_key=session_key)

    pay_id = request.GET["orderId"]

    data = get_status(pay_id)

    if data["status"] == "0":
        order = data["order"]

        email_send(order)

        text = f"Ваш заказ принят. Ему присвоен № {order.id}."

        session_key = request.session.session_key
        cart_items = Cart.objects.filter(session_key=session_key)
        request.session["delivery"] = 1
        order.paid = True
        cart_items.delete()
        order.save()

        return redirect("/?order=True")

    else:
        return redirect("order_error")

def order_succes(request):
  return render(request, "pages/orders/success.html")
