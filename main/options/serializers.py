from rest_framework import serializers

# import all models app content
from .models import *
 


class StorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Story
        fields = ('__all__')