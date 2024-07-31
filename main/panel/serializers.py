from rest_framework import serializers

from .models import *

from accounts.models import User
from options.models import Blog , Tag
from content.models import Product , GaleryProduct



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone','username','is_active','is_admin')


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


class BlogSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Blog 
        fields = ('__all__')

class TagSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Tag 
        fields = ('__all__')




    


