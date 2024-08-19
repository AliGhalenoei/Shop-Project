from rest_framework import serializers

# import all models app content
from .models import *
 


class StorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Story
        fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only =True)
    product = serializers.StringRelatedField(read_only =True)
    
    class Meta:
        model = CommentProduct
        fields = ('user' , 'product' , 'message' , 'is_reply')

class CreateUpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProduct
        fields = ('message',)

class ContactUsSerializer(serializers.Serializer):

    SUBJECT = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
        ('e','E'),
        ('f','F'),
        ('g','G'),
        ('h','H'),
    )

    email = serializers.EmailField(required = True)
    subject = serializers.ChoiceField(choices=SUBJECT)
    message = serializers.CharField(required=False)



