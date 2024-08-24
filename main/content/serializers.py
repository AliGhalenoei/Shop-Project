from rest_framework import serializers

from .models import *

# import modules app options
from panel.models import MenuNavbar
from options.models import *



class CategorysSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('__all__')


class SubCategorysSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ('__all__')


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only =True)
    sub_category = serializers.StringRelatedField(read_only =True)
    galerys = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('__all__')

    def get_galerys(self , obj):
        result = obj.galery.all()
        return GaleryProductSerializer(instance = result , many = True).data


class GaleryProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = GaleryProduct
        fields = ('__all__')


class BlogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('__all__')

    
class AddCartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuNavbar
        fields = ('__all__')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('__all__')