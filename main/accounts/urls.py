from django.urls import path 
from .import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Login and create token paths
    path('login/',views.UserLoginAPIView.as_view(),name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Logout
    path('logout/',views.UserLogoutAPIView.as_view(),name='logout'),
    # Register paths
    path('register/',views.UserRegisterAPIView.as_view(),name='register'),

]
