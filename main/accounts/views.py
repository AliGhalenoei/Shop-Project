from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    MyTokenObtainPairSerializer,
    UserLogoutSerializer
)
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
    

    
