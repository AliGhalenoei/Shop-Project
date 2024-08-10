from django.urls import path 
from .import views


urlpatterns = [
    # RUD User Model
    path('users/',views.UsersAPIView.as_view(),name='users'),
    path('user/<int:user_id>/',views.RetrieveUserAPIView.as_view(),name='user'),
    path('update/user/<int:user_id>/',views.UpdateUserAPIView.as_view(),name='update_user'),
    path('delete/user/<int:user_id>/',views.DeleteUserAPIView.as_view(),name='delete_user'),
    # CUD Product Model
    path('add/product/',views.CreateProductAPIView.as_view(),name='add_product'),
    path('update/product/<int:product_id>/',views.UpdateProductAPIView.as_view(),name='update_product'),
    path('delete/product/<int:product_id>/',views.DeleteProductAPIView.as_view(),name='delete_product'),
    # CUD GaleryProduct Model
    path('add/galery/product/<int:product_id>/',views.CreatGaleryProductAPIView.as_view(),name='add_galery_product'),
    path('update/galery/product/<int:galery_id>/',views.UpdateGaleryProductAPIView.as_view(),name='update_galery'),
    path('delete/galery/product/<int:galery_id>/',views.DeleteGaleryProductAPIView.as_view(),name='delete_galery'),
    # Reply comments and get all comments
    path('comments/',views.CommentsAPIView.as_view(),name='comments'),
    path('reply/comments/<int:product_id>/<int:comment_id>/',views.ReplyCommentProductAPIView.as_view(),name='comments'),
    # CRUD Blog Model
    path('add/blog/',views.CreateBlogAPIView.as_view(),name='add_blog'),
    path('update/blog/<int:blog_id>/',views.UpdateBlogAPIView.as_view(),name='update_blog'),
    path('delete/blog/<int:blog_id>/',views.DeleteBlogAPIView.as_view(),name='delete_blog'),
    # CRUD Tag Model
    path('tags/',views.TagsAPIView.as_view(),name='tags'),
    path('add/tag/',views.CreateTagAPIView.as_view(),name='add_tag'),
    path('tag/<int:tag_id>/',views.RetrieveTagAPIView.as_view(),name='tag'),
    path('update/tag/<int:tag_id>/',views.UpdateTagAPIView.as_view(),name='update_tag'),
    path('delete/tag/<int:tag_id>/',views.DeleteTagAPIView.as_view(),name='delete_tag'),
    # reply contacts
    path('contact/messages/',views.ContactMessagesAPIView.as_view(),name='contact_messages'),
    path('reply/contact/<int:contact_id>/',views.ReplyContactAPIView.as_view(),name='reply_contact'),
    

]
