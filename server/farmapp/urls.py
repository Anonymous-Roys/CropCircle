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
    path('api/product/<int:productId>/reviews', views.ProductReviewCreateView.as_view(), name='add-review')

]
