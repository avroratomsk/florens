from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q

from .services import *


from .models import *

def category(request):
  category = Category.objects.all()
  
  context = {
    "title": "Заголовок категорий",
    "category": category,
  }

  return render(request, "pages/catalog/category.html", context)


def category_detail(request, slug):
  category = Category.objects.get(slug=slug)
  products = Product.objects.filter(category=category)
  
  context = {
    "category_name": category.name,
    "title": "Название товара",
    "products": products
  }
  
  return render(request, "pages/catalog/category-details.html", context)

def product(request, slug):

  context = {
    "title": "Название продукта"
  }
  return render(request, "pages/catalog/product.html", context)
