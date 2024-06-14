from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny

from .serializers import *
from .models import *
# Create your views here.


class CategorysAPIView(APIView):

    """
        get all categorys
    """

    permission_classes = [AllowAny]
    serializer_class = CategorysSerializer

    def get(self , request):
        queryset = Category.objects.all()
        serializer = self.serializer_class(instance = queryset , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    
class ProductsAPIView(APIView):

    """
        get all Products
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def get(self , request):
        queryset = Product.objects.all()
        serializer = self.serializer_class(instance = queryset , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    

class RetrieveProductAPIView(APIView):

    """
        Taking a product using its slug. 
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def get(self , request , slug_product):
        queryset = Product.objects.get(slug = slug_product)
        serializer = self.serializer_class(instance = queryset)
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    

class FilterProductAPIView(APIView):

    """
    
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def get(self , request , slug_category):
        category = Category.objects.get(slug = slug_category)
        products = Product.objects.filter(category = category)
        serializer = self.serializer_class(instance = products , many=True)

        return Response(data = serializer.data , status = status.HTTP_200_OK)
