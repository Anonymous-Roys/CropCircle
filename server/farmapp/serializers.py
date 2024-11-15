from rest_framework import serializers
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
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    customerId = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='customer'))

    class Meta:
        model = Review
        fields = ['reviewId', 'product', 'customerId', 'rating', 'comment', 'createdAt', 'updatedAt']

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
