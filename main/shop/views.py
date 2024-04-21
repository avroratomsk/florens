from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
import itertools
from .services import *
from django.db.models import Max, Min

from .models import *

def category(request):
  category = Category.objects.all()
  
  for cat in category:
    cat.product_count = cat.product_set.count() # Получаем количество товаров в каждой категории
  
  context = {
    "title": "Заголовок категорий",
    "categorys": category,
  }

  return render(request, "pages/catalog/category.html", context)


def category_detail(request, slug):
  category = Category.objects.get(slug=slug)
  # chars = CharName.objects.filter(group=None)
  groups = CharGroup.objects.all()
  products = Product.objects.filter(category=category)
  max_price_product = Product.objects.filter(category=category).aggregate(Max('price'))['price__max']
  min_price_product = Product.objects.filter(category=category).aggregate(Min('price'))['price__min']
  
  
  if request.method == "GET":
    get_filtres = request.GET
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    
    
    if min_price != None and min_price != '':
      min_price = float(min_price)
      
    else:
      min_price = min_price_product
      print(min_price)
      print('-------------')
      
    if max_price != None and max_price != '':
      max_price = float(max_price)
      
    else:
      max_price = max_price_product
      print(max_price)
      print('-------------')
      
    
    char_filtres_list = list(get_filtres.keys())
    parametrs_value = []
    for parametr in char_filtres_list:
      parametrs_value.append(request.GET.getlist(parametr))# [['Малиновый', 'Белый'], ['25']]
    
    merged_array = list(itertools.chain(*parametrs_value))
    product = ProductChar.objects.filter(char_value__in=merged_array)
    
    id_filter = [pr.parent.id for pr in product]
    
    if id_filter:
        products = products.filter(id__in=id_filter, price__gte=min_price, price__lte=max_price)
    
  products_all = Product.objects.filter(status=True, category_id=category)
  chars_all = ProductChar.objects.filter(parent__in=products_all).distinct()
  char_name = CharName.objects.filter(c_chars__in=chars_all, filter_add=True).exclude(filter_name=None).distinct()
  
  chars_list_name_noduble = []
  for li in chars_all:
    if li.char_value not in chars_list_name_noduble:
      chars_list_name_noduble.append(li.char_value)
  
  chars = ProductChar.objects.filter(char_value__in=chars_list_name_noduble).distinct('char_value')
  
  chars_list_name_noduble_a = ProductChar.objects.filter(parent__in=products_all).distinct().values_list('char_value', flat=True).distinct()
  # print(chars_list_name_noduble_a)

  # chars = ProductChar.objects.filter(char_value__in=chars_list_noduble)
  # print(chars)
  
  context = {
    "category_name": category.name,
    "title": "Название товара",
    "products": products,
    "chars": chars,
    "char_name": char_name,
    "min_price_product": min_price_product,
    "max_price_product": max_price_product,
  }
  
  return render(request, "pages/catalog/category-details.html", context)

def product(request, slug):
  product = Product.objects.get(slug=slug)
  images = ProductImage.objects.filter(parent_id=product.id)[:3]
  products = Product.objects.filter(category_id=product.category.id).exclude(slug=slug)[:4]
  saleProducts = Product.objects.filter(sale_price__gt=0)[:4]
  
  context = {
    "title": "Название продукта",
    "product": product,
    "images": images,
    "products": products,
    "saleProducts": saleProducts
  }
  return render(request, "pages/catalog/product.html", context)
