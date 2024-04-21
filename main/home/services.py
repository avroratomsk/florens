from django.http import JsonResponse
import requests
import itertools

from home.models import Stock
from shop.models import CharGroup, CharName, Product, ProductChar

