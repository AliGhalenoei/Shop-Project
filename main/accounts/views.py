from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken 

from .serializers import (
    MyTokenObtainPairSerializer,
    UserLogoutSerializer,
    UserRegisterSerializer
)
from .utils import send_otp
from .models import OTP , User

import random
# Create your views here.



class UserLoginAPIView(TokenObtainPairView):
    """
        Create token and refresh_token and logined user

        Requeired filds:

        phone: 09.......

        password: your password....

        Note:

            token: Expires after one hour ⏰

            refresh_token: Expires after one day 🕒
    """
    serializer_class = MyTokenObtainPairSerializer


class UserLogoutAPIView(APIView):

    """
        In this view, the refresh_token expires ❌. 
        You should delete the access_token so that the user loses access. 👍🔒

        Note: 
        
            The user must be logged in. 💻🔒
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserLogoutSerializer

    def post(self , request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={'message':'User Logouted...'},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserRegisterAPIView(APIView):
    """
        create user and create token
        
        In this view, an account is created for the user. 

        Required fields:
        - phone
        - username
        - password
        - password2

        Note: An error will be displayed if the fields "Password" and "Password2" do not match.

    """

    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self , request):
        srz_data = self.serializer_class(data=request.data)

        if srz_data.is_valid():
            vd = srz_data.validated_data
            user = User.objects.create_user(
                phone = vd['phone'],
                username = vd['username'],
                password = vd['password']
            )
            refresh = RefreshToken.for_user(user)
            return Response({
                'phone':user.phone,
                'username':user.username,
                'password':user.phone,
                'role':user.is_admin,
                'user_id':user.id,
                'access':str(refresh.access_token),
                'refresh':str(refresh)
            } , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)