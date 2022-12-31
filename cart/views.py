from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from cart.serializers import CartSerializer
from notifications.models import Notification
from products.models import Product
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Cart


# class views
class CartView(APIView):
    """
    This view checks out the order
    """

    # schema = ProductSchema()

    # permissions
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """ Returns all available purchases """

    def get(self,request):
        orders = Cart.objects.all()
        serializer = CartSerializer(orders, many=True)
        return Response(serializer.data)

    """ Saves a new order """

    @csrf_exempt
    def post(self,request):

        data=request.data

        print(data)
        
        # Save each item in order as order
        items=data["items"]

        title="Items sold in shop"
        body=f""" The following items were sold in shop:\n\n"""

        for item in items:
            try:
                product=get_object_or_404(Product,id=item["product"])
                if product:
                    order=Cart.objects.create(item=product,quantity=item["quantity"])
                    order.save()
                    body += f"{order.quantity} {product.name}\n"

                    product.quantity -= item["quantity"]
                    product.save()   

                    #  Check if item goes below the minQuantity and do something about it
                    if product.quantity <= product.minQuantity or product.quantity - product.minQuantity <= 2:
                        Notification.objects.create(title="Low Stock!",body=f"{product.name}'s if falling below minimum stock!\n\nAvailable quantity is: {product.quantity}\nMinimum quantity is: {product.minQuantity}")

                    if product.quantity <= product.minQuantity:
                        # TODO! send alert
                        pass

            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        # Send a notification
        Notification.objects.create(title=title,body=body)

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        order = get_object_or_404(Cart, pk=request.data.get("order"))

        if order:
            order.delete()

            return Response({"message": "Order deleted successfully"})
        else:
            return Response({"message": "Failed to delete the order"})