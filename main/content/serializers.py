from rest_framework import serializers

# import all models app content
from .models import *



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




    

