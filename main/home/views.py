from django.http import HttpResponse
from django.shortcuts import redirect, render
import itertools
from home.models import AboutTemplate, BaseSettings, HomeTemplate, Questions, Slider, Stock
from cart.models import Cart
from home.forms import CallbackForm, QuickOrderForm
from home.callback_send import email_callback, email_quick_order
from shop.models import Category, CharGroup, CharName, Product, ProductChar
from reviews.models import Reviews
from django.http import HttpResponseRedirect


def callback(request):
  if request.method == "POST":
    form = CallbackForm(request.POST)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      message = form.cleaned_data['message']
      title = 'Заказ обратного звонка'
      messages = "Заказ обратного звонка:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone) + "\n" + "*Сообщение*: " +str(message)
      
      email_callback(messages, title)
      
      return redirect('callback_success')
  else:
    form = CallbackForm()
  
  context = {
    'form': form
  }
  
  return render(request, 'pages/index.html', context)

def quick_order(request):
  if request.method == "POST":
    form = QuickOrderForm(request.POST)
    print(form)
    if form.is_valid():
      name  = form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      product = form.cleaned_data['goods']
      title = 'Быстрый заказ'
      messages = "Быстрый заказ товара:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone) + "\n" + "*Название товара*: " +str(product)
      
      email_quick_order(messages, title)
      
      return redirect('callback_success')
  else:
    form = QuickOrderForm()
  context = {
    'form': form
  }
  
  
  return render(request, 'pages/index.html', context)

def callback_success(request):
  return render(request, "pages/orders/callback-succes.html")

def index(request):
  page = request.GET.get('page', 1)
  
  form = CallbackForm()
  
  try: 
    home_page = HomeTemplate.objects.get()
    settings = BaseSettings.objects.get()
  except:
    home_page = HomeTemplate.objects.all()
    settings = BaseSettings.objects.all()

  category = Category.objects.all()[:4]
  for cat in category:
    cat.product_count = cat.product_set.count() # Получаем количество товаров в каждой категории
    
  product = Product.objects.filter(quantity_purchase__gte=10)
  saleProduct = Product.objects.filter(sale_price__gt=0)[:8]
  affordable_products = Product.objects.filter(price__gt=0, price__lt=2500)[:8]
  reviews = Reviews.objects.filter(status=True)
  slider_image = Stock.objects.filter(status=True)
  questions = Questions.objects.filter(status=True)[:3]
  slide_about = Slider.objects.filter(status=True)
  
  context = {
    "categorys": category,
    "home_page": home_page,
    "products": product,
    "saleProduct": saleProduct,
    "affordable": affordable_products,
    "settings": settings,
    "reviews": reviews,
    "questions": questions,
    "slider_image": slider_image,
    "slide_about": slide_about,
    "form": form
  }
  return render(request, 'pages/index.html', context)

def populate(request):
  groups = CharGroup.objects.all()
  products = Product.objects.filter(quantity_purchase__gte=10)
  if request.method == "GET":
    get_filtres = request.GET
    char_filtres_list = list(get_filtres.keys())
    parametrs_value = []
    for parametr in char_filtres_list:
      parametrs_value.append(request.GET.getlist(parametr))# [['Малиновый', 'Белый'], ['25']]
    
    merged_array = list(itertools.chain(*parametrs_value))
    product = ProductChar.objects.filter(char_value__in=merged_array)
    
    id_filter = [pr.parent.id for pr in product]
    if id_filter:
        products = products.filter(id__in=id_filter)
  
  products_all = Product.objects.filter(status=True, quantity_purchase__gte=10)
  chars_all = ProductChar.objects.filter(parent__in=products_all).distinct()
  char_name = CharName.objects.filter(c_chars__in=chars_all, filter_add=True).exclude(filter_name=None).distinct()
  
  chars_list_name_noduble = []
  for li in chars_all:
    if li.char_value not in chars_list_name_noduble:
      chars_list_name_noduble.append(li.char_value)
  # print(chars_list_name_noduble)
  
  chars = ProductChar.objects.filter(char_value__in=chars_list_name_noduble).distinct('char_value')
  print(chars)
  
  chars_list_name_noduble_a = ProductChar.objects.filter(parent__in=products_all).distinct().values_list('char_value', flat=True).distinct()
  
  
  context = {
    "title": "Популярные товары",
    "products": products,
    "char_name": char_name,
    "chars": chars
  }
  
  return render(request, "pages/populate.html", context)

def best_offer(request):
  free_shipping_products = Product.objects.filter(free_shipping=True)
  
  context = {
    "title": "Лучшие предложения",
    "free_shipping_products": free_shipping_products
  }
  
  return render(request, "pages/best_offer.html", context)

def stock_product(request):
  products = Product.objects.filter(discount__gte=1)
  
  context = {
    "title": "Товары по акции",
    "products": products
  }
  
  return render(request, "pages/stock-product.html", context)

def news(request):
  products = Product.objects.filter(latest=True)
  
  groups = CharGroup.objects.all()
  if request.method == "GET":
    get_filtres = request.GET
    char_filtres_list = list(get_filtres.keys())
    parametrs_value = []
    for parametr in char_filtres_list:
      parametrs_value.append(request.GET.getlist(parametr))# [['Малиновый', 'Белый'], ['25']]
    
    merged_array = list(itertools.chain(*parametrs_value))
    product = ProductChar.objects.filter(char_value__in=merged_array)
    
    id_filter = [pr.parent.id for pr in product]
    if id_filter:
        products = products.filter(id__in=id_filter)
  
  products_all = Product.objects.filter(status=True, latest=True)
  chars_all = ProductChar.objects.filter(parent__in=products_all).distinct()
  char_name = CharName.objects.filter(c_chars__in=chars_all, filter_add=True).exclude(filter_name=None).distinct()
  
  chars_list_name_noduble = []
  for li in chars_all:
    if li.char_value not in chars_list_name_noduble:
      chars_list_name_noduble.append(li.char_value)
  # print(chars_list_name_noduble)
  
  chars = ProductChar.objects.filter(char_value__in=chars_list_name_noduble).distinct('char_value')
  
  chars_list_name_noduble_a = ProductChar.objects.filter(parent__in=products_all).distinct().values_list('char_value', flat=True).distinct()
  
  context = {
    "title": "Новинки",
    "products": products,
    "char_name": char_name,
    "chars": chars
  }
  
  return render(request, "pages/latest-product.html", context)

def about(request):
    form = CallbackForm()
    
    try:
      about_page = AboutTemplate.objects.get()
    except:
      about_page = AboutTemplate.objects.all()
    context = {
      "form": form,
      "about_page": about_page,
    }
    return render(request, "pages/about.html", context)

def contact(request):
  
    return render(request, "pages/contact.html")

def stock(request):
    stocks = Stock.objects.filter(status=True)
    news = Product.objects.filter(latest=True)
    populate = Product.objects.filter(quantity_purchase__gte=10)
    free_delivery = Product.objects.filter(free_shipping=True)
    
    context = {
        "stocks": stocks,
        "news": news,
        "populate": populate,
        "free_delivery": free_delivery,
    }
    
    return render(request, "pages/stock/stock.html", context)

def stock_detail(request, slug):
    stock = Stock.objects.get(slug=slug)
    
    context = {
        "stock": stock
    }
    
    return render(request, "pages/stock/stock_detail.html", context)


def questions(request):
  questions = Questions.objects.filter(status=True)
  
  context = {
    "questions": questions
  }
  
  return render(request, "pages/question.html", context)