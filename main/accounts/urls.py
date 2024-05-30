from django.urls import path 
from .import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/',views.UserLoginAPIView.as_view(),name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.UserLogoutAPIView.as_view(),name='logout'),
    # Register paths
    path('authentication/',views.UserAuthenticationAPIView.as_view(),name='authentication'),
    path('veryfy/code/',views.VeryfyOtpAPIView.as_view(),name='veryfy'),
    path('register/',views.UserRegisterAPIView.as_view(),name='register'),

]
