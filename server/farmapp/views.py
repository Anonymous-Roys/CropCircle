from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404
from .models import Product, Review, User, Farmer
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer, ProductSerializer, ProductCreateUpdateSerializer


class ProductReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, productId):
        # Ensure the product exists
        try:
            product = Product.objects.get(productId=productId)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # Prepare review data
        review_data = request.data
        review_data['product'] = productId  # Link the review to the product
        review_data['customerId'] = request.user.userId  # Set the customer to the current user

        # Validate and save the review
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FarmerProductsListView(APIView):
    def get(self, request, farmerId):
        # Fetch the Farmer instance by farmerId
        farmer = get_object_or_404(Farmer, pk=farmerId)
        # Retrieve all products for this farmer
        products = Product.objects.filter(farmer=farmer)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    def post(self, request, farmerId):
        # Fetch the Farmer instance
        farmer = get_object_or_404(Farmer, pk=farmerId)
        # Add farmer to the incoming data
        data = request.data
        data['farmer'] = farmer.farmerId  # Associate the product with the farmer
        
        # Serialize and validate the data
        serializer = ProductCreateUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(farmer=farmer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductCreateUpdateSerializer

    # Override lookup_field to use 'productId' instead of 'pk'
    lookup_field = 'productId'

    def get_queryset(self):
        # Get the queryset by filtering products by farmerId and productId
        farmerId = self.kwargs['farmerId']
        productId = self.kwargs['productId']  # Now we can use 'productId' instead of 'pk'
        return Product.objects.filter(farmer_id=farmerId, productId=productId)

    def update(self, request, *args, **kwargs):
        # Override update method to perform validation and save updated product
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
