from django.urls import path 
from .import views


urlpatterns = [
    path('storys/',views.StorysAPIView.as_view(),name='storys'),
]
