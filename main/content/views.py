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
        return Response(data = serializer.data , status=status.HTTP_200_OK , )


class SubCategorysAPIView(APIView):

    """
        get all sub categorys
    """

    permission_classes = [AllowAny]
    serializer_class = SubCategorysSerializer

    def get(self , request):
        queryset = SubCategory.objects.all()
        serializer = self.serializer_class(instance = queryset , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK , )
    
    
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
    

class FilterProductsByCategoryAPIView(APIView):

    """
        API view for filtering by sub_category.
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def setup(self, request, *args, **kwargs) :
        self.category_instance = Category.objects.get(slug = kwargs['slug_category'])
        self.product_instance = Product.objects.filter(category = self.category_instance)
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        products = self.product_instance
        serializer = self.serializer_class(instance = products , many=True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)
    

class FilterProductsBySubCategoryAPIView(APIView):

    """
        API view for filtering products by sub_category.
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def setup(self, request, *args, **kwargs) :
        self.subcategory_instance = SubCategory.objects.get(slug = kwargs['slug_subcategory'])
        self.product_instance = Product.objects.filter(sub_category = self.subcategory_instance)
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        products = self.product_instance
        serializer = self.serializer_class(instance = products , many=True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)


class RelatedProductAPIView(APIView):
    
    """
        In this view:
        the product slug is taken and suggests 8 products similar to the user's taste.
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(slug = kwargs['slug_product'])
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        product = self.product_instance
        object_list = Product.objects.filter(category = product.category.first())[:8]
        serializer = self.serializer_class(instance = object_list , many = True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)

