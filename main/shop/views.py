from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
import itertools
from .services import *
from django.db.models import Max, Min
from django.core.paginator import Paginator

from .models import *

def category(request):
  page = request.GET.get("page", 1)
  try: 
    shop_settings = ShopSettings.objects.get()
  except:
    shop_settings = ShopSettings()
  products = Product.objects.filter(status=True)
  # max_price_product = Product.objects.filter(status=True).aggregate(Max('price'))['price__max']
  # min_price_product = Product.objects.filter(status=True).aggregate(Min('price'))['price__min']
  
  
  if request.method == "GET":
    get_filtres = request.GET
    
    # if min_price != None and min_price != '':
    #   min_price = float(min_price)
      
    # else:
    #   min_price = min_price_product
      
    # if max_price != None and max_price != '':
    #   max_price = float(max_price)
      
    # else:
    #   max_price = max_price_product
      
    
    char_filtres_list = list(get_filtres.keys())
    parametrs_value = []
    for parametr in char_filtres_list:
      parametrs_value.append(request.GET.getlist(parametr))
    
    merged_array = list(itertools.chain(*parametrs_value))
    product = ProductChar.objects.filter(char_value__in=merged_array)
    
    id_filter = [pr.parent.id for pr in product]
    
    if id_filter:
        products = products.filter(id__in=id_filter)
    
  products_all = Product.objects.filter(status=True)
  paginator = Paginator(products, 15)
  current_page = paginator.page(int(page))
  chars_all = ProductChar.objects.filter(parent__in=products_all).distinct()
  char_name = CharName.objects.filter(c_chars__in=chars_all, filter_add=True).exclude(filter_name=None).distinct()
  
  chars_list_name_noduble = []
  for li in chars_all:
    if li.char_value not in chars_list_name_noduble:
      chars_list_name_noduble.append(li.char_value)
  
  chars = ProductChar.objects.filter(char_value__in=chars_list_name_noduble).distinct('char_value')
  
  context = {
    "shop_settings": shop_settings,
    "products": current_page,
    "chars": chars,
    "char_name": char_name,
    # "min_price_product": min_price_product,
    # "max_price_product": max_price_product,
  }

  return render(request, "pages/catalog/category.html", context)


def category_detail(request, slug):
  category = Category.objects.get(slug=slug)
  # chars = CharName.objects.filter(group=None)
  groups = CharGroup.objects.all()
  products = Product.objects.filter(category=category)
  # max_price_product = Product.objects.filter(category=category).aggregate(Max('price'))['price__max']
  # min_price_product = Product.objects.filter(category=category).aggregate(Min('price'))['price__min']
  
  
  if request.method == "GET":
    get_filtres = request.GET
    
    
    # if min_price != None and min_price != '':
    #   min_price = float(min_price)
      
    # else:
    #   min_price = min_price_product
    #   print(min_price)
    #   print('-------------')
      
    # if max_price != None and max_price != '':
    #   max_price = float(max_price)
      
    # else:
    #   max_price = max_price_product
    #   print(max_price)
    #   print('-------------')
      
    
    char_filtres_list = list(get_filtres.keys())
    parametrs_value = []
    for parametr in char_filtres_list:
      parametrs_value.append(request.GET.getlist(parametr))# [['Малиновый', 'Белый'], ['25']]
    
    merged_array = list(itertools.chain(*parametrs_value))
    product = ProductChar.objects.filter(char_value__in=merged_array)
    
    id_filter = [pr.parent.id for pr in product]
    
    if id_filter:
        products = products.filter(id__in=id_filter)
    
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
    # "min_price_product": min_price_product,
    # "max_price_product": max_price_product,
  }
  
  return render(request, "pages/catalog/category-details.html", context)

def product(request, slug):
 # Получение конкретного продукта по slug с подгрузкой связанной категории
  product = Product.objects.select_related('category').get(slug=slug)

  # Получение первых 3 изображений, связанных с продуктом
  images = ProductImage.objects.filter(parent_id=product.id)[:3]

  # Получение первых 4 продуктов в той же категории, исключая текущий продукт, с подгрузкой связанных категорий
  products = Product.objects.filter(category_id=product.category.id).exclude(slug=slug).select_related('category')[:4]

  # Получение первых 4 продуктов, у которых есть скидка (sale_price больше 0), с подгрузкой связанных категорий
  saleProducts = Product.objects.filter(sale_price__gt=0).select_related('category')[:4]
  
  context = {
    "title": "Название продукта",
    "product": product,
    "images": images,
    "products": products,
    "saleProducts": saleProducts
  }
  return render(request, "pages/catalog/product.html", context)
