from django.urls import path 
from .import views


urlpatterns = [
    path('categorys/',views.CategorysAPIView.as_view(),name = 'categorys'),
    
    path('products/',views.ProductsAPIView.as_view(),name = 'products'),
    path('product/<slug:slug_product>/',views.RetrieveProductAPIView.as_view(),name = 'product'),
    path('products/filter/<slug:slug_category>/',views.FilterProductAPIView.as_view(),name = 'filter_products'),
    path('related/products/<slug:slug_product>/',views.RelatedProductAPIView.as_view(),name = 'related_products'),
]
