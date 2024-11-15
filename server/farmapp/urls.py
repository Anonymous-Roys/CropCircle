from django.urls import path
from .views import (
    GetCustomerCart, 
    AddItemToCart, 
    UpdateItemQuantityInCart, 
    RemoveItemFromCart, 
    ClearCart
)

urlpatterns = [
    path('api/customer/<int:customerId>/cart', GetCustomerCart.as_view(), name='get_customer_cart'),
    path('api/customer/<int:customerId>/cart/items', AddItemToCart.as_view(), name='add_item_to_cart'),
    path('api/customer/<int:customerId>/cart/items/<int:productId>', UpdateItemQuantityInCart.as_view(), name='update_item_quantity'),
    path('api/customer/<int:customerId>/cart/items/<int:productId>', RemoveItemFromCart.as_view(), name='remove_item_from_cart'),
    path('api/customer/<int:customerId>/cart', ClearCart.as_view(), name='clear_cart'),
]
