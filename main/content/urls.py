from django.urls import path 
from .import views


urlpatterns = [
    path('categorys/',views.CategorysAPIView.as_view(),name = 'categorys'),
    path('subcategorys/',views.SubCategorysAPIView.as_view(),name = 'sub_categorys'),
    
    # Products list and detail products
    path('products/',views.ProductsAPIView.as_view(),name = 'products'),
    path('product/<slug:slug_product>/',views.RetrieveProductAPIView.as_view(),name = 'product'),

    # Filter products by category
    path('products/filter/<slug:slug_category>/',views.FilterProductsByCategoryAPIView.as_view(),name = 'filter_products'),
    # Filter products by sub_category
    path('products/filter/subcategory/<slug:slug_subcategory>/',views.FilterProductsBySubCategoryAPIView.as_view(),name = 'filter_subcategory'),

    path('related/products/<slug:slug_product>/',views.RelatedProductAPIView.as_view(),name = 'related_products'),
]
