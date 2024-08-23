from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny

from .serializers import *
from .models import *
from .cart import Cart

from options.models import CommentProduct


# Category and Sub_Category
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
    
# Product Model
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
    
class OfferProductsAPIView(APIView):

    """
        get offer Products
    """

    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer

    def get(self , request):
        queryset = Product.objects.filter(status = 'off')
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
        object_list = Product.objects.filter(category = product.category)[:8]
        serializer = self.serializer_class(instance = object_list , many = True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)


# blogs and detail blogs
class BlogsAPIView(APIView):

    """
        get all Blogs
    """

    permission_classes = [AllowAny]
    serializer_class = BlogsSerializer

    def setup(self, request, *args, **kwargs) :
        self.blog_instance = Blog.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        blogs = self.blog_instance
        serializer = self.serializer_class(instance = blogs , many = True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)
    
class RetrieveBlogAPIView(APIView):

    """
        retrieve Blogs
    """

    permission_classes = [AllowAny]
    serializer_class = BlogsSerializer

    def setup(self, request, *args, **kwargs) :
        self.blog_instance = Blog.objects.get(slug = kwargs['slug_blog'])
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        blog = self.blog_instance
        serializer = self.serializer_class(instance = blog)
        return Response(data = serializer.data , status = status.HTTP_200_OK)


# Cart
class CartAPIView(APIView):
    """
        Getting the users shopping cart
    """

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        cart = Cart(request)

        return Response(
            {"cart": list(cart.__iter__()), 
            "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )
    
class AddCartAPIView(APIView):

    """
            Adding a product to the shopping cart.

            Note: 
            
                If the product is already in the cart, it will increase the quantity.
    """

    permission_classes = [AllowAny]
    serializer_class = AddCartSerializer

    def get(self , request , product_id):
        product = Product.objects.get(id = product_id)
        cart = Cart(request)
        # serializer = self.serializer_class(data = request.data)

        cart.add_cart(product)
        return Response({
                'message':'add to cart successfuly',
                'cart':list(cart.__iter__()),
                "cart_total_price": cart.get_total_price()} ,
                status=status.HTTP_200_OK
                )
        # return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class RemoveCartAPIView(APIView):

    """
            Remove the product from the shopping cart.

            Note: 

                If the quantity of the products is more than 1, only the quantity will be decreased.
    """

    permission_classes = [AllowAny]

    def post(self , request , product_id):
        product = Product.objects.get(id = product_id)
        cart = Cart(request)
        cart.remove_cart(product)
        return Response({
                'cart':list(cart.__iter__()),
                "cart_total_price": cart.get_total_price()} ,
                status=status.HTTP_200_OK
                )

class ClearCartAPIView(APIView):

    """
        Remove the entire shopping cart. 
    """

    permission_classes = [AllowAny]

    def post(self, request):
        cart = Cart(request)
        cart.clear_cart()
        return Response({'message':'clear cart successfuly'} , status=status.HTTP_200_OK)
    
# Items MennuNavbar Model
class NavbarItemsAPIView(APIView):

    """
        get all items Navbar
    """

    permission_classes = [AllowAny]
    serializer_class = MenuItemSerializer

    def setup(self, request, *args, **kwargs) :
        self.menu_instance = MenuNavbar.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        menus = self.menu_instance
        serializer = self.serializer_class(instance = menus , many = True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)

