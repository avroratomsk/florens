from django.urls import path

from order import views

urlpatterns = [
    path('', views.order, name="order"),
    path('create/', views.order_create, name="order_create"), 
    # path('cart_change/', views.cart_change, name="cart_change"), 
    # path('cart_remove/', views.cart_remove, name="cart_remove"), 
]