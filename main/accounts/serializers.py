from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken , TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




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

    