from django.urls import path
from . import views

urlpatterns= [
    path('cart_list/', views.cart_list, name='cart_lst'),
    path('create_cart/', views.create_cart, name='create_cart'),
    path('cart_list/<int:id>/delete/', views.delete_cart_view, name='delete_cart'),
    path('cart_list/<int:id>/update/', views.update_cart_view, name='update'),
]