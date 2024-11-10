from django.contrib import admin
from .models import User, Farmer, Product, Order, OrderItem, Review, Notification


# Register User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'role', 'is_verified', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_verified')


admin.site.register(User, UserAdmin)


# Register Farmer model
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('farmer_id', 'user', 'business_license', 'farm_registration', 'verification_status')
    search_fields = ('user__username', 'business_license', 'farm_registration')
    list_filter = ('verification_status',)


admin.site.register(Farmer, FarmerAdmin)


# Register Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'farmer', 'name', 'price', 'quantity', 'status', 'harvest_date')
    search_fields = ('name', 'farmer__user__username')
    list_filter = ('status',)


admin.site.register(Product, ProductAdmin)


# Register Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'status', 'created_at')
    search_fields = ('customer__username',)
    list_filter = ('status',)


admin.site.register(Order, OrderAdmin)


# Register OrderItem model
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('product__name',)
    list_filter = ('order__status',)


admin.site.register(OrderItem, OrderItemAdmin)


# Register Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'rating', 'created_at')
    search_fields = ('customer__username', 'product__name')
    list_filter = ('rating',)


admin.site.register(Review, ReviewAdmin)


# Register Notification model
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'read_status', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('read_status',)


admin.site.register(Notification, NotificationAdmin)
