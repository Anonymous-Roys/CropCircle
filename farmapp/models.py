from django.db import models

# Create Users model
class User(models.Model):
    ADMIN = 'admin'
    FARMER = 'farmer'
    CUSTOMER = 'customer'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (FARMER, 'Farmer'),
        (CUSTOMER, 'Customer'),
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# Create Farmers model
class Farmer(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    VERIFICATION_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    farmer_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farmers')
    business_license = models.CharField(max_length=255, blank=True, null=True)
    farm_registration = models.CharField(max_length=255, blank=True, null=True)
    verification_status = models.CharField(max_length=10, choices=VERIFICATION_STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"Farmer: {self.user.username}"


# Create Products model
class Product(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    product_id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    harvest_date = models.DateField()
    image_url = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.name


# Create Orders model
class Order(models.Model):
    CONFIRMED = 'confirmed'
    PREPARING = 'preparing'
    DISPATCHED = 'dispatched'
    DELIVERED = 'delivered'
    STATUS_CHOICES = [
        (CONFIRMED, 'Confirmed'),
        (PREPARING, 'Preparing'),
        (DISPATCHED, 'Dispatched'),
        (DELIVERED, 'Delivered'),
    ]

    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CONFIRMED)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_id}"


# Create OrderItems model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item: {self.product.name} x {self.quantity}"


# Create Reviews model
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.username}"


# Create Notifications model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} at {self.created_at}"
