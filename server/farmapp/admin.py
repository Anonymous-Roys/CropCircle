from django.contrib import admin
from .models import (
    User,
    Farmer,
    Product,
    Order,
    Cart,
    Review,
    AdminActivityLog
)


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name', 'email', 'role', 'phone', 'createdAt', 'updatedAt')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('role',)
    readonly_fields = ('createdAt', 'updatedAt')
    ordering = ('-createdAt',)

# Farmer Model Admin
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('farmerId', 'user', 'farmName', 'location', 'farmType', 'verificationStatus', 'createdAt', 'updatedAt')
    search_fields = ('farmName', 'user__name', 'location')
    list_filter = ('verificationStatus', 'farmType')
    readonly_fields = ('createdAt', 'updatedAt')
    ordering = ('-createdAt',)

# Product Model Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productId', 'productName', 'farmer', 'category', 'unitPrice', 'stockQuantity', 'status', 'createdAt', 'updatedAt')
    search_fields = ('productName', 'farmer__farmName', 'category')
    list_filter = ('status', 'category')
    readonly_fields = ('createdAt', 'updatedAt')
    ordering = ('-createdAt',)

# Order Model Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderId', 'customer', 'totalAmount', 'status', 'createdAt', 'updatedAt')
    search_fields = ('customer__name',)
    list_filter = ('status',)
    readonly_fields = ('createdAt', 'updatedAt')
    ordering = ('-createdAt',)

# Cart Model Admin
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cartId', 'customer', 'totalPrice', 'createdAt', 'updatedAt')
    search_fields = ('customer__name',)
    readonly_fields = ('createdAt', 'updatedAt')
    ordering = ('-createdAt',)

# Review Model Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewId', 'product', 'customer', 'rating', 'createdAt', 'updatedAt')
    search_fields = ('product__productName', 'customer__name')
    list_filter = ('rating',)
    readonly_fields = ('createdAt', 'updatedAt')
    ordering = ('-createdAt',)

# Admin Activity Log Model Admin
@admin.register(AdminActivityLog)
class AdminActivityLogAdmin(admin.ModelAdmin):
    list_display = ('logId', 'admin', 'action', 'targetId', 'timestamp')
    search_fields = ('admin__name', 'action')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)