from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('item_delete/<int:product_id>/',views.item_delete,name='item_delete'),
]
