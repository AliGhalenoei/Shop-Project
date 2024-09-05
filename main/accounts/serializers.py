from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken , TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['phone'] = user.phone
        token['username'] = user.username
        token['password'] = user.password
        token['is_admin'] = user.is_admin
        # ...

        return token
    

class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
            return True   
             
        except TokenError:
            raise serializers.ValidationError('Bad Tokens...')


class UserRegisterSerializer(serializers.Serializer):
    phone = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate_phone(self , value):
        if User.objects.filter(phone = value).exists():
            raise serializers.ValidationError('The phone number was already exist!!!')
        elif len(value) > 11:
            raise serializers.ValidationError('The phone number is invalid')
        return value
    
    def validate_username(self , value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError('Username is already exist!!!')
        return value
    
    def validate(self,value):
        if value['password'] and value['password2'] and value['password'] != value['password2']:
            raise serializers.ValidationError('Passwords is not Match')
        return value


