from django.urls import path

from home import views

urlpatterns = [
    path('o-nas/', views.about, name="about"),
    path('contacts/', views.contact, name="contact"),
    path('akcii/', views.stock, name="stock"),
    path('akcii/<slug:slug>', views.stock_detail, name="stock_detail"),
    path('populate/', views.populate, name="populate"),
    path('stock/', views.stock_product, name="stock_product"),
    path('news/', views.news, name="news"),
    path('best-offer/', views.best_offer, name="best_offer"),
    path('questions/', views.questions, name="questions"),
    path('quick-order/', views.quick_order, name="quick_order"),
    path('callback/', views.callback, name="callback"),
    path('callback-success/', views.callback_success, name="callback_success"),
    
    path('', views.index, name="home"),
]