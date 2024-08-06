from django.contrib import admin
from django.urls import path
from . import views
from .views import updateItem



urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
   # path('update_item/', views.updateItem, name="updateItem"),
    path('update_item/', updateItem, name='update_item'),

]
