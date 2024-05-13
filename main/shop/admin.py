from admin.forms import ProductCharForm, ProductForm, ProductImageForm, ShopSettingsForm
from shop.models import CharName, Product, ProductChar, ProductImage, ShopSettings
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

'''

  В данном файле указаны все views которые
  отвечаю за функциональность вкладки магазин в админ панели
  
'''

def admin_shop(request):
  """Настройки магазина"""
  try:
    shop_setup = ShopSettings.objects.get()
    form = ShopSettingsForm(instance=shop_setup)
  except:
    form = ShopSettingsForm()
    
  if request.method == "POST":
    shop_setup = ShopSettings.objects.get()
    form_new = ShopSettingsForm(request.POST, request.FILES, instance=shop_setup)
    
    if form_new.is_valid:
      form_new.save()
      
      return redirect('admin_shop')
    else:
      return render(request, "shop/settings.html", {"form": form})
  
  context = {
    "form": form,
  }  
  return render(request, "shop/settings.html", context)


def admin_product(request):
  """
  View, которая возвращаяет и отрисовывает все товары на странице
  и разбивает их на пагинацию 
  """
  page = request.GET.get('page', 1)
  
  products = Product.objects.all()
  paginator = Paginator(products, 10)
  current_page = paginator.page(int(page))
  
  context = {
    "products": current_page
  }
  return render(request, "shop/product/product.html", context)

def product_edit(request, pk):
  """
    View, которая получает данные из формы редактирования товара
    и изменяет данные внесенные данные товара в базе данных
  """
  product = Product.objects.get(id=pk)
  form = ProductForm(instance=product)
  image_form = ProductImageForm()
  product_char_form = ProductCharForm()
  chars = ProductChar.objects.filter(parent_id=pk)
  all_chars = CharName.objects.all()
  
  form_new = ProductForm(request.POST, request.FILES, instance=product) 
  if request.method == 'POST':
    if form_new.is_valid():
      form_new.save()
      product = Product.objects.get(slug=request.POST['slug'])
      images = request.FILES.getlist('src')
      # Характеристики 
      char_name = request.POST.getlist('text_name')
      char_value = request.POST.getlist('char_value')
      char_count = 0

      for char in char_name:

          value = char_value[char_count]
          product_char = ProductChar(
              char_name_id = char,
              parent = product,
              char_value = value
          )
          product_char.save()
          char_count += 1

      old_char_id = request.POST.getlist('old_char_id')
      old_char_name = request.POST.getlist('old_text_name')
      old_char_value = request.POST.getlist('old_char_value')
      old_char_count = 0

      for id in old_char_id:

          old_char = ProductChar.objects.get(id=id)
          old_char.char_name_id = old_char_name[old_char_count]
          old_char.char_value = old_char_value[old_char_count]
          
          old_char.save()
          old_char_count += 1
      for image in images:
          img = ProductImage(parent=product, src=image)
          img.save()
      return redirect('admin_product')
    else:
      return render(request, 'shop/product/product_edit.html', {'form': form_new})
  context = {
    "form":form,
    'image_form': image_form,
    "product_char_form": product_char_form,
    "all_chars": all_chars,
    "chars": chars,
  }
  return render(request, "shop/product/product_edit.html", context)


def product_add(request):
  form = ProductForm()
  product_char_form = ProductCharForm()
  
  if request.method == "POST":
    form_new = ProductForm(request.POST, request.FILES)
    print('this')
    if form_new.is_valid():
      form_new.save()
      product = Product.objects.get(slug=request.POST['slug'])
      print(product)
      char_name = request.POST.getlist('text_name')
      print(char_name)
      char_value = request.POST.getlist('char_value')
      print(char_value)
      char_count = 0

      for char in char_name:

          value = char_value[char_count]
          product_char = ProductChar(
              char_name_id = char,
              parent = product,
              char_value = value
          )
          product_char.save()
          char_count += 1


      product.save()
      return redirect('admin_product')
    else:
      messages = "Форма не валидна"
      return render(request, "shop/product/product_add.html", {"form": form_new, "messages": messages})
    
  context = {
    "form": form,
    "product_char_form":product_char_form,
  }
  
  return render(request, 'shop/product/product_add.html', context)