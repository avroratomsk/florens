from django import forms
from home.models import AboutTemplate, BaseSettings, HomeTemplate, Slider, Stock, QuestionPage, Questions
from coupons.models import Coupon
from blog.models import BlogCategory, Post
from service.models import Service, ServicePage
from reviews.models import Reviews
from shop.models import Category, CharGroup, CharName, Product, ProductChar, ProductImage, ShopSettings
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from tinymce.widgets import TinyMCE

class UploadFileForm(forms.Form):
    file = forms.FileField()

class GlobalSettingsForm(forms.ModelForm):
  """ Form, глобальные и общие настройки сайта(лого, телефон, email)"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  class Meta:
    model = BaseSettings
    fields = "__all__"
    labels = {
        'logo': 'Логотип',
        'phone': 'Номер телефона',
        'time_work': 'Режим работы',
        'email': 'Email',
        'address': 'Адрес',
        'map_code': 'Код яндекс карты',
        'meta_h1':'Заголвок первого уровня',
        'meta_title':'Meta title',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
        'phone': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'time_work': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form__controls'
        }),
        'address': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'map_code': forms.Textarea(attrs={
            'class': 'form__controls'
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'meta_description': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls'
        }),
        'instagram': forms.TextInput(attrs={
          'class': 'form__controls'
        }),
        'telegram': forms.TextInput(attrs={
          'class': 'form__controls'
        }),
        'vk': forms.TextInput(attrs={
          'class': 'form__controls'  
        }),
        'viber': forms.TextInput(attrs={
          'class': 'form__controls' 
        }),
        'phone_whatsapp': forms.TextInput(attrs={
          'class': 'form__controls'
        }),
    }
    
class ProductForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Описание производителя', required=False, widget=CKEditorUploadingWidget)
    description = forms.CharField(widget=TinyMCE())
    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'description',
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
            # 'html_content',
            'image',
            'price',
            'diameter',
            'discount',
            'sale_price',
            'quantity_purchase',
            'quantity_flower',
            'quantity',
            'category',
            'composition',
            'width',
            'height',
            'image',
            'free_shipping',
            'status',
            'latest',
        ]
        labels = {
            'name': 'Название блюда',
            'slug':'URL',
            'meta_h1':'Заголвок первого уровня',
            'meta_title':'Meta title',
            'meta_description':'Мета description',
            'meta_keywords':'Meta keywords',
            'image':'Изображение',
            'price':'Цена',
            'diameter':'Диаметр',
            'sale_price':'Цена со скидкой',
            'composition':'Состав букета',
            'width':'Ширина',
            'height':'Высота',
            'quantity_purchase':'Количество покупок',
            'quantity_flower':'Количество цветков',
            'discount':'Скидка в (%)',
            'quantity':'Количество',
            'image': 'Превью изображения',
            'status': 'Статус публикации',
            'free_shipping': 'Бесплатная доставка',
            'latest': 'Новинка ?'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form__controls',
                "id":"name"
            }),
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'composition': forms.Textarea(attrs={
                'class': 'form__controls',
            }),
            'width': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'height': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form__controls',
                "id": "meta_description"
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'diameter': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'sale_price': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'quantity_purchase': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'quantity_flower': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form__controls',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form__controls',
                "id": "slug"
            }),
            'category': forms.CheckboxSelectMultiple(attrs={
                'class': 'form__controls', 
            }),
            'free_shipping': forms.CheckboxInput(attrs={
            }),
            'weight': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'discount': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            # 'image': forms.FileInput(attrs={
            #     'class': 'submit-file',
            #     'accept': 'image/*'
            # }),
        }
        
class ShopSettingsForm(forms.ModelForm):
    """ Form, отвечает за создание товара и редактирование товара"""
    # description = forms.CharField(label='Описание производителя', required=False, widget=CKEditorUploadingWidget)
    description = forms.CharField(widget=TinyMCE())
    class Meta:
        model = ShopSettings
        fields = [
            'meta_h1',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]
        labels = {
            'meta_h1':'Заголвок первого уровня',
            'meta_title':'Meta title',
            'meta_description':'Мета description',
            'meta_keywords':'Meta keywords',
        }
        widgets = {
            'meta_h1': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form__controls',
                "id": "meta_description"
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
        }

# Товар и опции товара
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage

        fields = [
            'parent',
            'src'
        ]
        labels = {
            'src': 'Выбрать изображение'
        }
        widgets = {
            'parent': forms.Select(attrs={
                'class': 'form__controls', 
            })
        }



class CategoryForm(forms.ModelForm):
  """ Form, отвечает за создание категорий и редактирование категорий"""
  class Meta:
    model = Category
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      }),
      "description": forms.Textarea(attrs={
        "class":"form__controls",
      }),
      'menu_add': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      # 'image': forms.FileInput(attrs={
      #     'class': 'submit-file',
      #     'accept': 'image/*'
      # }),
      "meta_h1": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Заголовок H1"
      }),
      "meta_title": forms.TextInput(attrs={
        "class":"form__controls meta_field",
        "id": "meta_title"
        # "placeholder": "Meta заголовок"
      }),
      "meta_description": forms.Textarea(attrs={
        "class":"form__controls meta_field",
        # "placeholder": "Meta Описание",
        "rows": "5"
      }),
      "meta_keywords": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Meta keywords"
      }),  
    }
    
# class DayForm(forms.ModelForm):
#   """ Form, отвечает за создание дней и редактирование дней"""
#   class Meta:
#     model = Day
#     fields = [
#       "name",
#       "slug"
#     ]
#     labels = {
#       "name": "Назване категории",
#       "slug": "URL",
#     }
#     widgets = {
#       "name": forms.TextInput(attrs={
#           "class": "form__controls",
#           "id":"name"
#           # "placeholder": "Название  категории"
#       }),
#       "slug": forms.TextInput(attrs={
#         "class":"form__controls",
#         "id": "slug"
#         # "placeholder": "Название категори"
#       })
#     }
    
# class FillialForm(forms.ModelForm):
#   """ Form, отвечает за добавление филлиала и редактирование филлиала"""
#   class Meta:
#     model = Subsidiary
#     fields = [
#       "name",
#       "address_fillial",
#       "image",
#       "slug"
#     ]
#     labels = {
#       "name": "Название филлиала",
#       "address_fillial": "Адрес филлиала",
#       "image": "Фотография зала",
#       "slug": "URL",
#     }
#     widgets = {
#       "name": forms.TextInput(attrs={
#           "class": "form__controls",
#           "id":"name"
#       }),
#       "address_fillial": forms.TextInput(attrs={
#           "class": "form__controls",
#           "id":"name",
#           "placeholder": "г.Томск, ул.Ленина 111"
#       }),
#       "slug": forms.TextInput(attrs={
#         "class":"form__controls",
#         "id": "slug"
#       })
#     }
    
class HomeTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  about_text = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = HomeTemplate
      fields = [
          'banner',
          'meta_h1',
          'untitle',
          'meta_title',
          'meta_description',
          'meta_keywords',
          'about_text',
          'about_image'
      ]
      labels = {
          'banner': 'Изображение банера',
          'meta_h1':'Заголвок первого уровня',
          'meta_title':'Meta title',
          'untitle': 'Надзаголовок',
          'meta_description':'Мета description',
          'meta_keywords':'Meta keywords',
          'about_text':'Текст о нас',
          'about_image':'Изображение о нас'
      }
      widgets = {
          'name': forms.TextInput(attrs={
              'class': 'form__controls'
          }),
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'untitle': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_title': forms.TextInput(attrs={
              'class': 'form__controls',
              # 'placeholder': 'Мета заголовок',
          }),
          'meta_description': forms.TextInput(attrs={
              'class': 'form__controls',
              # 'placeholder': 'Мета описание',
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          # 'about_text': forms.TextInput(attrs={
          #     'class': 'form__controls',
          # }),
      }
class AboutTemplateForm(forms.ModelForm):
  """ Form, редактирование главной страницы"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  about_text = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
      model = AboutTemplate
      fields = [
          'banner',
          'meta_h1',
          'meta_title',
          'meta_description',
          'meta_keywords',
          'about_text',
      ]
      labels = {
          'banner': 'Изображение банера',
          'meta_h1':'Заголвок первого уровня',
          'meta_title':'Meta title',
          'meta_description':'Мета description',
          'meta_keywords':'Meta keywords',
          'about_text':'Текст о нас',
      }
      widgets = {
          'meta_h1': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_title': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_description': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'meta_keywords': forms.TextInput(attrs={
              'class': 'form__controls',
          }),
          'about_text': forms.Textarea(attrs={
              'class': 'form__controls',
              'rows': 5
          }),
      }
           
class ReviewsForm(forms.ModelForm):
  """ Form, добавление и редактирование отзыва"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Reviews
    fields = [
        'avatar',
        'name',
        'slug',
        'date',
        'text',
        'status',
        'meta_h1',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'avatar': 'Фотография пользователя',
        'name':'ФИО пользователя',
        'slug': 'URL',
        'date':'Дата коментария',
        'text':'Текст коментария',
        'status':'Статус публикации',
        'meta_h1':'Заголвок первого уровня',
        'meta_title':'Meta title',
        'untitle': 'Надзаголовок',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'date': forms.DateInput(attrs={
        'class':'form__controls',
      }),
      'text': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_h1': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
    
class StockForm(forms.ModelForm):
  """ Form, добавление и редактирование акций"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Stock
    fields = [
        'title',
        'slug',
        'description',
        'home_slider',
        'status',
        'slider_status',
        'link',
        'image',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'title':'Название акции',
        'slug': 'URL',
        'home_slider':'Вывести в слайдер на главную',
        'link':'Ссылка',
        'description':'Текст коментария',
        'status':'Статус публикации',
        'slider_status':'Вывод на главный слайдер',
        'image': 'Изображение акции',
        'meta_title':'Meta title',
        'untitle': 'Надзаголовок',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'title': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'link': forms.TextInput(attrs={
        'class':'form__controls',
      }),
      'description': forms.Textarea(attrs={
        'class': 'form__controls',
        'rows': 5,
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'home_slider': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'slider_status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }

class ServicePageForm(forms.ModelForm):
  """ Поля настроек старницы услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Service
    fields = [
        'name',
        'slug',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'name':'Название',
        'slug': 'URL',
        'meta_title':'Meta title',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }  
    
class ServiceForm(forms.ModelForm):
  """ Form, добавление и редактирование услуг"""
  # description = forms.CharField(label='Полное описание товара', required=False, widget=CKEditorUploadingWidget())
  
  class Meta:
    model = Service
    fields = [
        'name',
        'slug',
        'subtitle',
        'status',
        'image',
        'meta_title',
        'meta_description',
        'meta_keywords',
    ]
    labels = {
        'name':'Название',
        'slug': 'URL',
        'subtitle':'Текст под заголовком',
        'status':'Статус публикации',
        'image': 'Изображение акции',
        'meta_title':'Meta title',
        'untitle': 'Надзаголовок',
        'meta_description':'Мета description',
        'meta_keywords':'Meta keywords',
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form__controls',
        'id': 'name'
      }),
      'slug': forms.TextInput(attrs={
        'class':'form__controls',
        "id": "slug"
      }),
      'subtitle': forms.Textarea(attrs={
        'class':'form__controls',
      }),
      'status': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      'meta_title': forms.TextInput(attrs={
        'class': 'form__controls',
      }),
      'meta_description': forms.Textarea(attrs={
        'class': 'form-controls',
        'rows': 5,
      }),
      'meta_keywords': forms.TextInput(attrs={
        'class': 'form__controls'
      })
    }
    
class ProductCharForm(forms.ModelForm):
    class Meta:
        model = ProductChar
        fields = [
            'char_name',
            'char_value',
        ]
        labels = {
            'char_name': 'Название характеристики',
            'char_value': 'Значение',
        }
        widgets = {
            'char_name': forms.Select(attrs={
                'class': 'form__controls',
                'placeholder': 'Название характеристики',
                'id': 'id_char_name',
               
            }),
            'char_value': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Значение',
                'id': 'id_char_value'
            }),
        }

class CharGroupForm(forms.ModelForm):
    class Meta:
        model = CharGroup
        fields = [
            'name',
        ]
        labels = {
            'name': 'Название группы характеристик',
           
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form__controls',
            }),
        }


class CharNameForm(forms.ModelForm):
  class Meta:
    model = CharName
    fields = [
        'group',
        'text_name',
        'filter_add',
        'filter_name',
        'sort_order'
        
    ]
    labels = {
        'group': 'Группа опций',
        'text_name': 'Название опции',
        'filter_add': "Добавить в фильтрацию",
        'filter_name': "Название фильтрации на английском",
        'sort_order': "Сортировка"
    }
    widgets = {
        'group': forms.Select(attrs={
          'class': 'form__controls'
        }),
        'text_name': forms.TextInput(attrs={
            'class': 'form__controls',
            'id': 'char_name'
        }),
        'filter_add': forms.CheckboxInput(attrs={
            'class': 'form__controls-checkbox',
        }),
        'filter_name': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'sort_order': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
    }
    
    
class QuestionPageForm(forms.ModelForm):
  class Meta:
    model = QuestionPage
    fields = [
        'meta_title',
        'meta_h1',
        'meta_description',
        'meta_keywords',
        
    ]
    labels = {
        'meta_title': 'Группа опций',
        'meta_h1': 'Название опции',
        'meta_description': "Добавить в фильтрацию",
        'meta_keywords': "Название фильтрации на английском",
    }
    widgets = {
        'meta_title': forms.TextInput(attrs={
            'class': 'form__controls-checkbox',
        }),
        'meta_h1': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'meta_description': forms.Textarea(attrs={
            'class': 'form__controls',
        }),
        'meta_keywords': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
    }
    
class QuestionsForm(forms.ModelForm):
  class Meta:
    model = Questions
    fields = [
        'title',
        'description',
        'status',
        
    ]
    # labels = {
    #     'title': 'Группа опций',
    #     'description': 'Название опции',
    #     'status': "Добавить в фильтрацию",
    # }
    widgets = {
        'meta_title': forms.CheckboxInput(attrs={
            'class': 'form__controls-checkbox',
        }),
        'title': forms.TextInput(attrs={
            'class': 'form__controls',
        }),
        'description': forms.Textarea(attrs={
            'class': 'form__controls',
        })
    }
    
class SliderForm(forms.ModelForm):
  class Meta:
    model = Slider
    fields = [
        'image',
        'status',
        
    ]
    widgets = {
        'status': forms.CheckboxInput(attrs={
            'class': 'form__controls-checkbox',
        }),
    }
    
class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = "__all__"
        labels = {
            'code': 'Код купона',
            'valid_from': 'Дата начала акции',
            'valid_to': 'Дата окончания акции',
            'discount': 'Скидка',
            'active': 'Активность',
        }
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form__controls',
                'placeholder': 'Код купона',
            }),
            'valid_from': forms.DateInput(attrs={
                'class': 'form__controls',
                'type': 'date',
                
            }),
            'valid_to': forms.DateInput(attrs={
                'class': 'form__controls',
                'type': 'date',
                
            }),

            
            'discount': forms.NumberInput(attrs={
                'class': 'form__controls',
                'placeholder': 'Скидка',
            }),
           
            
        }
        
        
class BlogCategoryForm(forms.ModelForm):
  """ Form, отвечает за создание категорий и редактирование категорий"""
  class Meta:
    model = BlogCategory
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      }),
      "description": forms.Textarea(attrs={
        "class":"form__controls",
      }),
      'menu_add': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      # 'image': forms.FileInput(attrs={
      #     'class': 'submit-file',
      #     'accept': 'image/*'
      # }),
      "meta_h1": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Заголовок H1"
      }),
      "meta_title": forms.TextInput(attrs={
        "class":"form__controls meta_field",
        "id": "meta_title"
        # "placeholder": "Meta заголовок"
      }),
      "meta_description": forms.Textarea(attrs={
        "class":"form__controls meta_field",
        # "placeholder": "Meta Описание",
        "rows": "5"
      }),
      "meta_keywords": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Meta keywords"
      }),  
    }
    
class BlogPostForm(forms.ModelForm):
  """ Form, отвечает за создание категорий и редактирование категорий"""
  class Meta:
    model = Post
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={
          "class": "form__controls",
          "id":"name"
          # "placeholder": "Название  категории"
      }),
      "slug": forms.TextInput(attrs={
        "class":"form__controls",
        "id": "slug"
        # "placeholder": "Название категори"
      }),
      "description": forms.Textarea(attrs={
        "class":"form__controls",
      }),
      'menu_add': forms.CheckboxInput(attrs={
        'class': 'form__controls-checkbox',
      }),
      # 'image': forms.FileInput(attrs={
      #     'class': 'submit-file',
      #     'accept': 'image/*'
      # }),
      "meta_h1": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Заголовок H1"
      }),
      "meta_title": forms.TextInput(attrs={
        "class":"form__controls meta_field",
        "id": "meta_title"
        # "placeholder": "Meta заголовок"
      }),
      "meta_description": forms.Textarea(attrs={
        "class":"form__controls meta_field",
        # "placeholder": "Meta Описание",
        "rows": "5"
      }),
      "meta_keywords": forms.TextInput(attrs={
        "class":"form__controls",
        # "placeholder": "Meta keywords"
      }),  
    }