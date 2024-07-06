from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny

from .serializers import *
from .models import *

# Create your views here.


class StorysAPIView(APIView):

    """
        get all storys
    """

    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def get(self , request):
        storys = Story.objects.all() 
        serializer = self.serializer_class(instance = storys , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)

