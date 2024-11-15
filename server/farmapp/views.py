from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404
from .models import Product, Review, User, Farmer
from .serializers import ReviewSerializer, ProductSerializer, ProductCreateUpdateSerializer


class ProductReviewCreateView(APIView):
    def post(self, request, productId):
        # Log the incoming data for debugging
        print("Request Data:", request.data)

        # Extract customerId, rating, and comment from the request data
        customer_id = request.data.get('customerId')  # Adjust based on field name in payload
        rating = request.data.get('rating')
        comment = request.data.get('comment')
        
        # Validate required fields
        if rating is None or comment is None or customer_id is None:
            raise ValidationError("Missing required fields: rating, comment, or customerId.")
        
        # Validate rating range: 1-5
        if not (1 <= int(rating) <= 5):
            raise ValidationError("Rating must be between 1 and 5.")

        # Fetch product and customer instance based on the passed IDs
        product = get_object_or_404(Product, productId=productId)  # Corrected this line
        customer = get_object_or_404(User, userId=customer_id, role='customer')  # customerId should match userId

        # Prepare data for serialization (pass the customer and product references)
        review_data = {
            'product': product,  # Ensure 'product' field is passed as the actual product object
            'customer': customer,  # Ensure 'customer' field is passed as the actual customer object
            'rating': rating,
            'comment': comment
        }

        # Use ReviewSerializer to handle review creation and validation
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"review": serializer.data}, status=status.HTTP_201_CREATED)
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
