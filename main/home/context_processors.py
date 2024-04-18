from home.models import BaseSettings
from shop.models import Category 
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

def header_menu(request):
    return {'header_menu': Category.objects.filter(menu_add=True)[:4]}

def category_list(request):
    return {'category_list': Category.objects.all()}