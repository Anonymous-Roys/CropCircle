from django.urls import path
from . import views

urlpatterns = [
    # For listing products for a specific farmer
    path('api/farmer/<int:farmerId>/products/', views.FarmerProductsListView.as_view(), name='farmer-products-list'),
    
    # For creating a product for a specific farmer
    path('api/farmer/<int:farmerId>/products', views.ProductCreateView.as_view(), name='product-create'),
    
    # For updating a product for a specific farmer
    path('api/farmer/<int:farmerId>/products/<int:productId>', views.ProductUpdateView.as_view(), name='product-update'),

    #For making a product review
    path('api/product/<int:productId>/reviews', views.ProductReviewCreateView.as_view(), name='add-review'),

     # URL for retrieving order details
    path("api/farmer/<int:farmerId>/orders/<int:orderId>", OrderDetailView.as_view(), name="order-detail"),
    
    # URL for updating order status
    path("api/farmer/<int:farmerId>/orders/<int:orderId>/status", UpdateOrderStatusView.as_view(), name="update-order-status"),
    
    # URL for deleting an order (or marking it as cancelled, depending on logic)
    path("api/farmer/<int:farmerId>/orders/<int:orderId>/delete", DeleteOrderView.as_view(), name="delete-order"),

    # URL for deleting a review
    path("api/product/<int:productId>/reviews/<int:reviewId>", DeleteReviewView.as_view(), name="delete-review"),

]

   
