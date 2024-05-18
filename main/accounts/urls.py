from django.urls import path 
from .import views

urlpatterns = [
    path('login/',views.UserLoginAPIView.as_view(),name='login'),

    path('logout/',views.UserLogoutAPIView.as_view(),name='logout'),

    # Register paths
    
]
