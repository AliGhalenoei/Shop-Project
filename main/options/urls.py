from django.urls import path 
from .import views


urlpatterns = [
    path('storys/',views.StorysAPIView.as_view(),name='storys'),
    
    # comment products
    path('comment/products/<slug:product_id>/',views.CommentProductsAPIView.as_view(),name = 'comment_products'),
    path('add/comment/<int:product_id>/',views.CreateCommentAPIView.as_view(),name='add_comment'),
    path('update/comment/<int:comment_id>/',views.UpdateCommentProductAPIView.as_view(),name='update_comment'),
    path('delete/comment/<int:comment_id>/',views.DeleteCommentProductAPIView.as_view(),name='delete_comment'),

    # Contact Us
    path('contact/',views.ContactUsAPIView.as_view(),name = 'contact'),
]
