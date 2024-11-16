from rest_framework import serializers
from .models import Order, Product
from .models import Product, Farmer, Review, User

class ProductSerializer(serializers.ModelSerializer):
    productId = serializers.IntegerField()
    productName = serializers.CharField()
    quantity = serializers.IntegerField(source='stockQuantity')
    price = serializers.DecimalField(source='unitPrice', max_digits=10, decimal_places=2)
    description = serializers.CharField()
    imageUrl = serializers.ImageField(source='productImage', required=False)
    status = serializers.CharField()
    dateAdded = serializers.DateTimeField(source='createdAt')

    class Meta:
        model = Product
        fields = ['productId', 'productName', 'quantity', 'price', 'description', 'imageUrl', 'status', 'dateAdded']


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    productName = serializers.CharField()
    quantity = serializers.IntegerField(source='stockQuantity')
    price = serializers.DecimalField(source='unitPrice', max_digits=10, decimal_places=2)
    description = serializers.CharField()
    imageUrl = serializers.ImageField(source='productImage', required=False)
    status = serializers.CharField()

    class Meta:
        model = Product
        fields = ['productName', 'quantity', 'price', 'description', 'imageUrl', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['reviewId', 'product', 'customerId', 'rating', 'comment', 'createdAt', 'updatedAt']
        read_only_fields = ['reviewId', 'createdAt', 'updatedAt']

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying detailed information about an order.
    
    Fields:
        - orderId: The unique ID of the order.
        - customerName: Name of the customer who placed the order.
        - productName: Name of the product in the order.
        - quantity: Quantity of the product ordered.
        - totalPrice: Total price of the order.
        - orderStatus: Status of the order.
        - dateOrdered: The date the order was placed.
        - deliveryDate: The expected delivery date for the order.
        - address: Address of the customer.
        - phone: Contact phone number of the customer.
    """
    orderId = serializers.IntegerField()  # Removed 'source' argument
    customerName = serializers.CharField(source='customer.name')
    productName = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    totalPrice = serializers.DecimalField(source='totalAmount', max_digits=10, decimal_places=2)
    orderStatus = serializers.CharField(source='status')
    dateOrdered = serializers.DateTimeField(source='createdAt')
    deliveryDate = serializers.DateTimeField()
    address = serializers.CharField(source='customer.address')
    phone = serializers.CharField(source='customer.phone', allow_null=True, required=False)

    def get_productName(self, obj):
        """
        Retrieves the name of the product from the Product model based on productId.
        Assumes that each order item is structured to include 'productId' in orderItems.
        """
        product_ids = [item['productId'] for item in obj.orderItems]
        products = Product.objects.filter(productId__in=product_ids)
        return ', '.join([product.productName for product in products])

    def get_quantity(self, obj):
        """
        Retrieves the quantity of the product ordered.
        Assumes 'quantity' is part of each entry in orderItems.
        """
        return sum(item.get('quantity', 0) for item in obj.orderItems)

    class Meta:
        model = Order
        fields = ['orderId', 'customerName', 'productName', 'phone', 'orderItems', 'totalPrice', 'orderStatus', 'address', 'quantity', 'dateOrdered', 'deliveryDate']




class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating the status of an order.
    
    Fields:
        - status: New status for the order, validated against allowed transitions.
    """

    status = serializers.ChoiceField(choices=Order.ORDER_STATUS_CHOICES)

    def validate_status(self, value):
        """
        Validates allowed status transitions for the order.
        """
        current_status = self.instance.status
        allowed_transitions = {
            'pending': ['shipped', 'cancelled'],
            'shipped': ['delivered'],
            'delivered': [],
        }

        if value not in allowed_transitions.get(current_status, []):
            raise serializers.ValidationError(
                f"Invalid status transition from '{current_status}' to '{value}'"
            )
        return value

    class Meta:
        model = Order
        fields = ['status']
