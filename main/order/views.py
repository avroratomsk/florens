from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect, render
from cart.models import Cart
from order.models import Order, OrderItem
from order.forms import CreateOrderForm
from django.contrib.auth.decorators import login_required

def order(request):
  ...
  
def order_create(request):
  if request.method == 'POST':
    form = CreateOrderForm(data=request.POST)
    if form.is_valid():
      try:
        with transaction.atomic():
          if request.user.is_authenticated:
            user = request.user
            cart_items = Cart.objects.filter(user=user)

            if cart_items.exists():
                # Создать заказ
                order = Order.objects.create(
                    user=user,
                    phone_number=form.cleaned_data['phone_number'],
                    requires_delivery=form.cleaned_data['requires_delivery'],
                    delivery_address=form.cleaned_data['delivery_address'],
                    payment_on_get=form.cleaned_data['payment_on_get'],
                )
                # Создать заказанные товары
                for cart_item in cart_items:
                    product=cart_item.product
                    name=cart_item.product.name
                    price=cart_item.product.sell_price()
                    quantity=cart_item.quantity


                    if product.quantity < quantity:
                        raise ValidationError(f'Недостаточное количество товара {name} на складе | В наличии - {product.quantity}')

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        name=name,
                        price=price,
                        quantity=quantity,
                    )
                    product.quantity -= quantity
                    product.save()

                # Очистить корзину пользователя после создания заказа
                cart_items.delete()
                print("Авторизован")
                messages.success(request, 'Заказ оформлен!')
                return redirect('order_succes')
          else:
            session_key=request.session.session_key
            cart_items = Cart.objects.filter(session_key=session_key)

            if cart_items.exists():
                # Создать заказ
                order = Order.objects.create(
                    phone_number=form.cleaned_data['phone_number'],
                    requires_delivery=form.cleaned_data['requires_delivery'],
                    delivery_address=form.cleaned_data['delivery_address'],
                    payment_on_get=form.cleaned_data['payment_on_get'],
                )
                # Создать заказанные товары
                for cart_item in cart_items:
                    product=cart_item.product
                    name=cart_item.product.name
                    price=cart_item.product.sell_price()
                    quantity=cart_item.quantity


                    if product.quantity < quantity:
                        raise ValidationError(f'Недостаточное количество товара {name} на складе | В наличии - {product.quantity}')

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        name=name,
                        price=price,
                        quantity=quantity,
                    )
                    product.quantity -= quantity
                    product.save()

                # Очистить корзину пользователя после создания заказа
                cart_items.delete()
                print("не Авторизован")
                messages.success(request, 'Заказ оформлен!')
                return redirect('order_succes')
      except ValidationError as e:
        print(e)
        messages.success(request, str(e))
        return redirect('order_create')
  else:
    initial = {
      # 'first_name': request.user.first_name,
      'first_name': "first_name",
      # 'last_name': request.user.last_name,
      'last_name': "last_name",
      }
    form = CreateOrderForm(initial=initial)

  context = {
    'title': 'Home - Оформление заказа',
    'form': form,
    'orders': True,
  }
  return render(request, 'pages/orders/create.html', context)

def order_succes(request):
  return render(request, "pages/orders/success.html")
