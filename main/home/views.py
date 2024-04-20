from django.http import HttpResponse
from django.shortcuts import render

from home.models import BaseSettings, HomeTemplate, Questions, Stock
from cart.models import Cart
from shop.models import Category, Product
from reviews.models import Reviews




def index(request):
  page = request.GET.get('page', 1)
  
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
  }
  return render(request, 'pages/index.html', context)

def populate(request):
  products = Product.objects.filter(quantity_purchase__gte=10)
  
  
  
  context = {
    "title": "Популярные товары",
    "products": products,
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
  
  context = {
    "title": "Новинки",
    "products": products
  }
  
  return render(request, "pages/latest-product.html", context)

def about(request):
    return render(request, "pages/about.html")

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