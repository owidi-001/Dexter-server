from django.shortcuts import get_object_or_404
from notifications.models import Notification
# from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ProductForm
from .models import Product, ProductImage
from .schema import ProductSchema
from .serializers import ProductImageSerializer, ProductSerializer

"""
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
HTTP_208_ALREADY_REPORTED
HTTP_226_IM_USED
"""

# class views
class ProductView(APIView):
    """
    List all products and CRUD operations for detail view for the product
    """

    schema = ProductSchema()
    # permissions
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """ Returns all available products """

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    """ Creates a new product """

    def post(self,request):
        # print(request.data)

        form=ProductForm(request.data)

        if form.is_valid():
            product=form.save(commit=False)
            product.created_by=request.user
            product.save()

            # Get the image data sent and save product image
            image=request.data.get("image")
            ProductImage.objects.create(product=product,image=image)

            serializer=ProductSerializer(product).data
            return Response(serializer,status=status.HTTP_201_CREATED)
            
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


    """ Updates existing product"""

    def patch(self, request):

        form = ProductForm(request.data)
        print(form.errors)


        if form.is_valid():
            product = get_object_or_404(Product, id=request.data.get("product"))
            
            old_name=product.name
            old_price=product.price
            old_quantity=product.quantity
            old_minQuantity=product.minQuantity
            old_type=product.type

            if form.cleaned_data.get("name"):
                product.name = form.cleaned_data.get("name")

            if form.cleaned_data.get("price"):
                product.unit_price = form.cleaned_data.get("price")

            if form.cleaned_data.get("quantity"):
                product.quantity = form.cleaned_data.get("quantity")
            
            if form.cleaned_data.get("minQuantity"):
                product.minQuantity = form.cleaned_data.get("minQuantity")

            if form.cleaned_data.get("type"):
                product.type = form.cleaned_data.get("type")
            
            
            product.save()

            # Update product image if any
            if form.cleaned_data.get("image"):
                if form.cleaned_data.get("image") != "empty":
                    product_image=ProductImage.objects.get_or_create(product=product,image=request.data.get("image"))[0]
                    product_image.save()


            # Create a notification message
            title="Product Update"
            body=f"""The following attributes of {product.name} were updated:\n\n"""

            if old_name != product.name:
                body += f"Name: From {old_name} -> {product.name}\n"

            if old_price != product.price:
                body += f"Price: From {old_price} -> {product.price}\n"

            if old_quantity != product.quantity:
                body += f"Quantity: From {old_quantity} -> {product.quantity}\n"
            
            if old_minQuantity != product.minQuantity:
                body += f"Min quantity: From {old_minQuantity} -> {product.minQuantity}\n"

            if old_type != product.type:
                body += f"Type: from {old_type} -> {product.type}\n"

            Notification.objects.create(title=title,body=body)

            serializer = ProductSerializer(product).data

            return Response(serializer,status=status.HTTP_202_ACCEPTED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    
    """ deletes a product from db """

    def delete(self, request):
        product = get_object_or_404(Product, pk=request.data.get("product"))

        if product:
            serializer=ProductSerializer(product).data
            
            product.delete()

            return Response(serializer,status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProductImageView(APIView):
    schema = ProductSchema()
    # permissions
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """ Returns all available product images """

    def get(self,request):
        images = ProductImage.objects.all()
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)