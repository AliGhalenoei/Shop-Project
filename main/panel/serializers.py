from rest_framework import serializers

from .models import *

from accounts.models import User
from options.models import *
from content.models import *


# User Serializers
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone','username','is_active','is_admin')

# Product Serializers
class GaleryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = GaleryProduct
        fields = ('image',)

class UpdateGaleryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = GaleryProduct
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Product 
        fields = ('__all__')

class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = CommentProduct
        fields = ('__all__')

class ReplyCommentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProduct
        fields = ('message',)

# Blogs serializers
class BlogSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Blog 
        fields = ('__all__')

class TagSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Tag 
        fields = ('__all__')

# Reply Contacts Serializer
class ReplyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyContact
        fields = ('message',)

class MessageContactSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only =True)
    
    class Meta:
        model = ContactUs
        fields = ('__all__')

# Add or Update categorys
class AddCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title','baner')
        extra_kwargs = {'title': {'required': True}} 

class UpdateCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title','baner')
        
# Add or Update sub_categorys
class AddSubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ('title','baner')
        extra_kwargs = {'title': {'required': True}} 

class UpdateSubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ('title','baner')
        
# add Story 
class AddStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('__all__')

# Menu Navbar Serializer
class MenuNavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuNavbar
        fields = ('__all__')

# View_by products      
class ViewsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('view_by',)


