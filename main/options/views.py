from django.core.mail import send_mail
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny

from .serializers import *
from .models import *

# Create your views here.


class StorysAPIView(APIView):

    """
        get all storys.
    """

    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def get(self , request):
        storys = Story.objects.all() 
        serializer = self.serializer_class(instance = storys , many = True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)


# comment products
class CommentProductsAPIView(APIView):

    """
        In this view:
        comments get from related to each product
    """

    permission_classes = [AllowAny]
    serializer_class = CommentSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(id = kwargs['product_id'])
        self.comments_instance = self.product_instance.com_products.all()
        return super().setup(request, *args, **kwargs)

    def get(self , request , *args , **kwargs):
        comments = self.comments_instance
        serializer = self.serializer_class(instance = comments, many=True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)
    
class CreateCommentAPIView(APIView):

    """
        In this view:
        create comment from product
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CreateUpdateCommentSerializer

    def setup(self, request, *args, **kwargs) :
        self.product_instance = Product.objects.get(id = kwargs['product_id'])
        return super().setup(request, *args, **kwargs)

    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            vd = serializer.validated_data
            CommentProduct.objects.create(
                user = request.user,
                product = self.product_instance,
                message = vd['message']
            )
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UpdateCommentProductAPIView(APIView):

    """
        update comments
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CreateUpdateCommentSerializer

    def setup(self, request, *args, **kwargs) :
        self.comment_instance = CommentProduct.objects.get(id = kwargs['comment_id'])
        return super().setup(request, *args, **kwargs)
    
    
    def put(self , request , *args , **kwargs):
        serializer = self.serializer_class(instance = self.comment_instance ,data = request.data , partial = True)

        if serializer.is_valid():
            if self.comment_instance.user.id == request.user.id:
                serializer.save()
                return Response(data = serializer.data ,status=status.HTTP_200_OK)
            else:
                return Response({'message':"You can update just your comment"})
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class DeleteCommentProductAPIView(APIView):

    """
        delete comments
        Note:

            The user must be logged in and is_admin must be active.
    """

    permission_classes = [IsAuthenticated]

    def setup(self, request, *args, **kwargs) :
        self.comment_instance = CommentProduct.objects.get(id = kwargs['comment_id'])
        return super().setup(request, *args, **kwargs)

    def delete(self , request , *args , **kwargs):
        comment = self.comment_instance

        if comment.user.id == request.user.id:
            comment.delete()
            return Response({'message':'comment deleted...'})
        else:
            return Response({'message' : 'You can delete just your comment'})

# Contact Us
class ContactUsAPIView(APIView):

    """
        Contact Us
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ContactUsSerializer

    def post(self , request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            vd = serializer.validated_data
            ContactUs.objects.create(
                user = request.user,
                email = vd.get('email'),
                subject = vd.get('subject'),
                message = vd.get('message')
            )
            
            # send email 
            msg = "you recieved an email from {0} \n related to : {1} \n message : {2}".format(
                vd['email'],
                vd['subject'],
                vd.get('message')
            )
            send_mail(
                subject=vd['subject'],
                message=msg,
                from_email=vd['email'],
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )
           
            return Response(data = serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
