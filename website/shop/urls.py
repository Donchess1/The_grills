from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/', views.add_product, name='add_product'),
    path('signup/', views.signup, name='signup'),
]
