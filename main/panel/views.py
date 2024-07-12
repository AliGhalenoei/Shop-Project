from django.utils.text import slugify

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import  MultiPartParser , FormParser , JSONParser
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser

from .permissions import IsAdmin
from .serializers import *
from .models import *

from accounts.models import *




# CRUD User Model
class UsersAPIView(APIView):

    """
        get all users

        Note:

            The user must be logged in and is_admin must be active. 
    """

    users_serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    
    def setup(self, request, *args, **kwargs) :
        self.user_instance = User.objects.all()
        return super().setup(request, *args, **kwargs)
    
    def get(self , request ):
        users = self.user_instance
        serializer = self.users_serializer_class(instance = users , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)

class RetrieveUserAPIView(APIView):

    """
        Retrieve users
        Note:

            The user must be logged in and is_admin must be active.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.user_instance = User.objects.get(id = kwargs['user_id'])
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        user = self.user_instance
        serializer = self.serializer_class(instance = user)
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    
class UpdateUserAPIView(APIView):

    """
        Update information users
        Note:

            The user must be logged in and is_admin must be active.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.user_instance = User.objects.get(id = kwargs['user_id'])
        return super().setup(request, *args, **kwargs)

    def put(self , request , *args , **kwargs):
        user = self.user_instance
        serializer = self.serializer_class(instance = user , data = request.data , partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class DeleteUserAPIView(APIView):

    """
        Delete account users
        Note:

            The user must be logged in and is_admin must be active.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.user_instance = User.objects.get(id = kwargs['user_id'])
        return super().setup(request, *args, **kwargs)

    def delete(self , request , *args , **kwargs):
        user = self.user_instance
        user.delete()
        return Response({'Message':'User Deleted...'},status=status.HTTP_200_OK)



# CRUD Product Model
class CreateProductAPIView(APIView):

    """
        Create Products
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = ProductSerializer

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UpdateProductAPIView(APIView):

    """
        Update products
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = ProductSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(id = kwargs['product_id'])
        return super().setup(request, *args, **kwargs)

    def put(self ,request , *args , **kwargs):
        queryset = self.product_instance
        serializer = self.serializer_class(instance = queryset, data = request.data , partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteProductAPIView(APIView):

    """
        Delete products
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = ProductSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(id = kwargs['product_id'])
        return super().setup(request, *args, **kwargs)

    def delete(self , request , *args, **kwargs):
        product = self.product_instance
        product.delete()
        return Response({'Message':'Product Deleted...'},status=status.HTTP_200_OK)



# CRUD GaleryProduct Model
class CreatGaleryProductAPIView(APIView):
    
    """
        Create GaleyProducts
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = GaleryProductSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(id = kwargs['product_id'])
        return super().setup(request, *args, **kwargs)

    def post(self , request , *args, **kwargs):
        product = self.product_instance
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save(product = product)            
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
       
class UpdateGaleryProductAPIView(APIView):

    """
        Update GaleryProducts
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = UpdateGaleryProductSerializer

    def setup(self, request, *args, **kwargs) :
        self.galery_instance = GaleryProduct.objects.get(id = kwargs['galery_id'])
        return super().setup(request, *args, **kwargs)
    
    def put(self , request , *args, **kwargs):
        galery = self.galery_instance
        serializer = self.serializer_class(instance = galery , data = request.data , partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class DeleteGaleryProductAPIView(APIView):

    """
        delete GaleryProducts
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = ProductSerializer

    def setup(self, request, *args, **kwargs) :
        self.galery_instance = GaleryProduct.objects.get(id = kwargs['galery_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        galery = self.galery_instance 
        galery.delete()
        return Response({'Message':'Galery Deleted...'},status=status.HTTP_200_OK)



# CRUD Blog Model
class CreateBlogAPIView(APIView):

    """
        Create Blog
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = BlogSerializer
    
    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save(slug = slugify(serializer.validated_data['title']))
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class UpdateBlogAPIView(APIView):

    """
        update Blogs
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = BlogSerializer

    def setup(self, request, *args, **kwargs) :
        self.blog_instance = Blog.objects.get(id = kwargs['blog_id'])
        return super().setup(request, *args, **kwargs)
    
    def put(self , request , *args, **kwargs):
        blog = self.blog_instance
        serializer = self.serializer_class(instance = blog , data = request.data , partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteBlogAPIView(APIView):

    """
        delete Blogs
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.blog_instance = Blog.objects.get(id = kwargs['blog_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        blog = self.blog_instance 
        blog.delete()
        return Response({'Message':'Blog Deleted...'},status=status.HTTP_200_OK)