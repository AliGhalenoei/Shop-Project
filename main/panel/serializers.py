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
    class Meta:
        model = ContactUs
        fields = ('__all__')




    


