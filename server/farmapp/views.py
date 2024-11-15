from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cart, Product, User

class GetCustomerCart(APIView):
    def get(self, request, customerId):
        # Fetch the customer's cart
        cart = get_object_or_404(Cart, customer__userId=customerId)

        # Manually create a response dictionary
        response_data = {
            "cartId": cart.cartId,
            "customerId": cart.customer.userId,
            "items": cart.items,
            "totalPrice": cart.totalPrice,
            "createdAt": cart.createdAt,
            "updatedAt": cart.updatedAt,
        }
        return Response(response_data, status=status.HTTP_200_OK)

class AddItemToCart(APIView):
    def post(self, request, customerId):
        product_id = request.data.get('productId')
        quantity = request.data.get('quantity')

        if not product_id or not quantity or quantity <= 0:
            return Response({"error": "Invalid productId or quantity."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch or create the cart for the customer
        customer = get_object_or_404(User, userId=customerId, role='customer')
        cart, created = Cart.objects.get_or_create(customer=customer)

        # Update or add the item in the cart
        items = cart.items or []
        item_found = False

        for item in items:
            if item['productId'] == int(product_id):
                item['quantity'] += int(quantity)
                item_found = True

        if not item_found:
            items.append({'productId': int(product_id), 'quantity': int(quantity)})

        # Save the updated cart
        cart.items = items
        cart.totalPrice = self.calculate_total_price(cart)
        cart.save()

        # Manually create a response dictionary
        response_data = {
            "cartId": cart.cartId,
            "updatedCart": {
                "items": cart.items,
                "totalPrice": cart.totalPrice,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    def calculate_total_price(self, cart):
        total = 0
        for item in cart.items:
            product = get_object_or_404(Product, productId=item['productId'])
            total += product.unitPrice * item['quantity']
        return total

class UpdateItemQuantityInCart(APIView):
    def put(self, request, customerId, productId):
        quantity = request.data.get('quantity')
        if not quantity or quantity < 0:
            return Response({"error": "Quantity must be a positive integer."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Fetch the customer's cart
        cart = get_object_or_404(Cart, customer__userId=customerId)
        
        # Update the item quantity or return an error if the item doesn't exist
        items = cart.items or []
        item_found = False
        for item in items:
            if item['productId'] == int(productId):
                item['quantity'] = quantity
                item_found = True
        
        if not item_found:
            return Response({"error": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)
        
        # Remove the item if the quantity is set to 0
        if quantity == 0:
            items = [item for item in items if item['productId'] != int(productId)]
        
        # Save the updated cart
        cart.items = items
        cart.totalPrice = self.calculate_total_price(cart)
        cart.save()

        # Manually create a response dictionary
        response_data = {
            "updatedCart": {
                "items": cart.items,
                "totalPrice": cart.totalPrice,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

class RemoveItemFromCart(APIView):
    def delete(self, request, customerId, productId):
        # Fetch the customer's cart
        cart = get_object_or_404(Cart, customer__userId=customerId)
        
        # Remove the item or return an error if the item doesn't exist
        items = cart.items or []
        items = [item for item in items if item['productId'] != int(productId)]
        
        # Save the updated cart
        cart.items = items
        cart.totalPrice = self.calculate_total_price(cart)
        cart.save()

        # Manually create a response dictionary
        response_data = {
            "updatedCart": {
                "items": cart.items,
                "totalPrice": cart.totalPrice,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

class ClearCart(APIView):
    def delete(self, request, customerId):
        # Fetch the customer's cart
        cart = get_object_or_404(Cart, customer__userId=customerId)
        
        # Clear the cart
        cart.items = []
        cart.totalPrice = 0
        cart.save()

        # Manually create a response dictionary
        response_data = {
            "updatedCart": {
                "items": [],
                "totalPrice": 0,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)



