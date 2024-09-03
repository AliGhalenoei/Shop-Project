from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import  MultiPartParser , FormParser , JSONParser
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser

from .permissions import IsAdmin
from .serializers import *
from .models import *

from accounts.models import *
from options.models import *

from content.serializers import FAQSerializer

import uuid

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
        
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

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


# Reply comment and get all comments
class CommentsAPIView(APIView):

    """
        get all comments
    """

    permission_classes = [IsAdmin]
    serializer_class = CommentsSerializer

    def setup(self, request, *args, **kwargs) :
        self.comment_instance = CommentProduct.objects.all()
        return super().setup(request, *args, **kwargs)
    
    def get(self , request , *args , **kwargs):
        comments = self.comment_instance
        serializer = self.serializer_class(instance = comments , many = True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)

class ReplyCommentProductAPIView(APIView):
    """
        reply comment products
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = ReplyCommentProductSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(id = kwargs['product_id'])
        self.comment_instance = CommentProduct.objects.get(id = kwargs['comment_id'])
        return super().setup(request, *args, **kwargs)

    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            vd = serializer.validated_data
            if request.user.is_admin:
                CommentProduct.objects.create(
                    user = request.user,
                    product = self.product_instance,
                    reply = self.comment_instance,
                    is_reply = True,
                    message = vd['message']
                )
                self.comment_instance.reply_complete = True
                self.comment_instance.save()
                return Response(data = serializer.data ,status=status.HTTP_200_OK)
            else:
                return Response({'message':'you not admin'})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


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
    
    
# CRUD Tag Model
class TagsAPIView(APIView):
    """
        get all Tags

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    
    def setup(self, request, *args, **kwargs) :
        self.tag_instance = Tag.objects.all()
        return super().setup(request, *args, **kwargs)
    
    def get(self , request):
        tags = self.tag_instance
        serializer = self.serializer_class(instance = tags , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)

class CreateTagAPIView(APIView):

    """
        Create Tag
        Note:

            The user must be logged in and is_admin must be active.
    """

    serializer_class = TagSerializer
    permission_classes = [IsAdmin]

    def post(self , request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class RetrieveTagAPIView(APIView):

    """
        Retrieve tags
        Note:

            The user must be logged in and is_admin must be active.
    """

    serializer_class = TagSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.tag_instance = Tag.objects.get(id = kwargs['tag_id'])
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        tag = self.tag_instance
        serializer = self.serializer_class(instance = tag)
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    
class UpdateTagAPIView(APIView):

    """
        update Tags
        Note:

            The user must be logged in and is_admin must be active.
    """

    serializer_class = TagSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.tag_instance = Tag.objects.get(id = kwargs['tag_id'])
        return super().setup(request, *args, **kwargs)
    
    def put(self , request , *args, **kwargs):
        tag = self.tag_instance
        serializer = self.serializer_class(instance = tag , data = request.data , partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteTagAPIView(APIView):

    """
        delete Tags
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.tag_instance = Tag.objects.get(id = kwargs['tag_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        self.tag_instance.delete()
        return Response({'Message':'Tag Deleted...'},status=status.HTTP_200_OK)
    
# Reply Contacts
class ContactMessagesAPIView(APIView):
    """
        get all contact us messages

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = MessageContactSerializer
    permission_classes = [IsAdmin]
    
    def setup(self, request, *args, **kwargs) :
        self.contact_instance = ContactUs.objects.all()
        return super().setup(request, *args, **kwargs)
    
    def get(self , request):
        messages = self.contact_instance
        serializer = self.serializer_class(instance = messages , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    
class ReplyContactAPIView(APIView):

    """
        Reply Contacts
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]
    serializer_class = ReplyContactSerializer

    def setup(self, request, *args, **kwargs) :
        self.contact_instance = ContactUs.objects.get(id = kwargs['contact_id'])
        return super().setup(request, *args, **kwargs)

    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data)
        contact = self.contact_instance

        if serializer.is_valid():
            from_email = settings.EMAIL_HOST_USER
            vd = serializer.validated_data
            reply = ReplyContact.objects.create(
                user = request.user,
                contact = contact,
                message = vd['message']
            )
            # reply email...
            msg = "you recieved an email from {0} \n related to : {1} \n message : {2}".format(
                from_email,
                reply.contact.subject,
                vd['message'],
            )
            send_mail(
                reply.contact.subject,
                message=msg,
                from_email=from_email,
                recipient_list=[reply.contact.email],
                fail_silently=False
            )
            contact.is_reply = True
            contact.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


# CUD Category Model
class AddCategoryAPIView(APIView):

    """
        add category

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = AddCategorySerializer
    permission_classes = [IsAdmin]

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            vd = serializer.validated_data
            uniqied_slug = str(uuid.uuid4())
            Category.objects.create(
                title = vd['title'],
                baner = vd['baner'],
                slug = uniqied_slug
            )
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UpdateCategoryAPIView(APIView):

    """
        update category

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = UpdateCategorySerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs):
        self.category_instance = Category.objects.get(id=kwargs['category_id'])
        return super().setup(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.category_instance, data=request.data, partial=True)

        if serializer.is_valid():
            vd = serializer.validated_data
            
            # Get title from validated data or fallback to the current title
            title = vd.get('title', self.category_instance.title)
            serializer.save(slug=slugify(title))
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DelteCategoryAPIView(APIView):

    """
        delete category

        Note:

            The user must be logged in and is_admin must be active. 
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs):
        self.category_instance = Category.objects.get(id=kwargs['category_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        self.category_instance.delete()
        return Response({'Message':'category Deleted...'},status=status.HTTP_200_OK)


# CUD Sub_Category Model
class AddSubCategoryAPIView(APIView):

    """
        add sub_category

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = AddSubCategorySerializer
    permission_classes = [IsAdmin]

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            vd = serializer.validated_data
            uniqied_slug = str(uuid.uuid4())
            SubCategory.objects.create(
                title = vd['title'],
                baner = vd['baner'],
                slug = uniqied_slug
            )
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UpdateSubCategoryAPIView(APIView):

    """
        update sub_category

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = UpdateSubCategorySerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs):
        self.sub_instance = SubCategory.objects.get(id=kwargs['sub_id'])
        return super().setup(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.sub_instance, data=request.data, partial=True)

        if serializer.is_valid():
            vd = serializer.validated_data
            
            # Get title from validated data or fallback to the current title
            title = vd.get('title', self.sub_instance.title)
            serializer.save(slug=slugify(title))
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DelteSubCategoryAPIView(APIView):

    """
        delete category

        Note:

            The user must be logged in and is_admin must be active. 
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs):
        self.sub_instance = SubCategory.objects.get(id=kwargs['sub_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        self.sub_instance.delete()
        return Response({'Message':'sub_category Deleted...'},status=status.HTTP_200_OK)


# Add or Delete Story Model
class AddStoryAPIView(APIView):

    """
        add Story

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = AddStorySerializer
    permission_classes = [IsAdmin]

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteStoryAPIView(APIView):

    """
        delete story
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.story_instance = Story.objects.get(id = kwargs['story_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        self.story_instance.delete()
        return Response({'Message':'Story Deleted...'},status=status.HTTP_200_OK)


# CUD Menu Navbar
class AddMenusAPIView(APIView):

    """
        add Menu to navbar

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = MenuNavbarSerializer
    permission_classes = [IsAdmin]

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class UpdateMenusAPIView(APIView):

    """
        update Menus

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = MenuNavbarSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs):
        self.menu_instance = MenuNavbar.objects.get(id=kwargs['menu_id'])
        return super().setup(request, *args, **kwargs)
    
    def put(self , request , *args , **kwargs):
        serializer = self.serializer_class(instance = self.menu_instance , data = request.data , partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteMenusAPIView(APIView):

    """
        delete menu
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.menu_instance = MenuNavbar.objects.get(id = kwargs['menu_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        self.menu_instance.delete()
        return Response({'Message':'Menu Deleted...'},status=status.HTTP_200_OK)


# CUD FAQ
class AddFAQ_APIView(APIView):

    """
        add Faqs

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = FAQSerializer
    permission_classes = [IsAdmin]

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class UpdateFAQ_APIView(APIView):

    """
        update faqs

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = FAQSerializer
    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs):
        self.faq_instance = FAQ.objects.get(id=kwargs['faq_id'])
        return super().setup(request, *args, **kwargs)
    
    def put(self , request , *args , **kwargs):
        serializer = self.serializer_class(instance = self.faq_instance , data = request.data , partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteFAQs_APIView(APIView):

    """
        delete faqs
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAdmin]

    def setup(self, request, *args, **kwargs) :
        self.faq_instance = FAQ.objects.get(id = kwargs['faq_id'])
        return super().setup(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        self.faq_instance.delete()
        return Response({'Message':'FAQ Deleted...'},status=status.HTTP_200_OK)


# View By Products
class ViewProductsAPIView(APIView):

    """
        Show all view products

        Note:

            The user must be logged in and is_admin must be active. 
    """

    serializer_class = ViewsProductSerializer
    permission_classes = [IsAdmin]

    def get(self , request):
        views = Product.objects.all().order_by('-view_by')
        serializer = self.serializer_class(instance=views , many = True)
        return Response(data = serializer.data ,status=status.HTTP_200_OK)

        
            
        