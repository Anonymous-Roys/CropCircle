from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone


# 1. User Model
class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Password field
    password = models.CharField(max_length=255)  # Password field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    reset_password_token = models.CharField(max_length=36, null=True, blank=True)  # UUID token
    reset_token_created_at = models.DateTimeField(null=True, blank=True)  # Token timestamp
    last_login = models.DateTimeField(null=True, blank=True)  # Last login timestamp

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'User'
        managed = True

# 2. Farmer Model
class Farmer(models.Model):
    VERIFICATION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    farmerId = models.AutoField(primary_key=True)
    userId = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'farmer'}, related_name='farmer', db_column='userId')
    farmName = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    farmType = models.CharField(max_length=50)
    certifications = models.TextField(null=True, blank=True)
    verificationStatus = models.CharField(max_length=10, choices=VERIFICATION_STATUS_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.farmName 
    
    class Meta:
        db_table = 'Farmer'
        managed = True

# 3. Product Model
class Product(models.Model):
    PRODUCT_STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('under_review', 'Under Review'),
    ]
    
    productId = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, db_column='farmerId')
    productName = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    stockQuantity = models.IntegerField()
    productImage = models.ImageField(upload_to='product_images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS_CHOICES, default='in_stock')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName
    
    class Meta:
        db_table = 'Product'
        managed = True

# 4. Order Model
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    # orderId = models.AutoField(primary_key=True)
    # customer = models.ForeignKey(User, on_delete=models.CASCADE, db_column='customerId')
    orderId = models.AutoField(primary_key=True)  # Primary key field
    customer = models.ForeignKey(User, on_delete=models.CASCADE, db_column='customerId')  # ForeignKey to User model
    orderItems = models.JSONField()  # Store an array of products, including productId, quantity, and price
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deliveryDate = models.DateTimeField(null=True, blank=True) 
    deliveryDate = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return str(self.orderId)
    
    class Meta:
        db_table = 'Order'
        managed = True

# 5. Cart Model (for Customers)
class Cart(models.Model):
    cartId = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    items = models.JSONField()  # Store an array of items, including productId and quantity
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cartId)
    
    class Meta:
        db_table = 'Cart'
        managed = True

# 6. Review Model
class Review(models.Model):
    reviewId = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.reviewId)
    
    class Meta:
        db_table = 'Review'
        managed = True

# 7. Admin Activity Log Model
class AdminActivityLog(models.Model):
    logId = models.AutoField(primary_key=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    action = models.CharField(max_length=255)
    targetId = models.IntegerField()  # ID of the target entity (e.g., farmerId or productId)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.action
    
    class Meta:
        db_table = 'AdminActivityLog'
        managed = True
