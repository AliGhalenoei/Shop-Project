from django.urls import path 
from .import views


urlpatterns = [
    path('categorys/',views.CategorysAPIView.as_view(),name = 'categorys'),
    path('subcategorys/',views.SubCategorysAPIView.as_view(),name = 'sub_categorys'),
    # Products list and detail products
    path('products/',views.ProductsAPIView.as_view(),name = 'products'),
    path('offer/products/',views.OfferProductsAPIView.as_view(),name = 'offer_products'),
    path('product/<slug:slug_product>/',views.RetrieveProductAPIView.as_view(),name = 'product'),
    # Filter products by category
    path('products/filter/<slug:slug_category>/',views.FilterProductsByCategoryAPIView.as_view(),name = 'filter_products'),
    # Filter products by sub_category
    path('products/filter/subcategory/<slug:slug_subcategory>/',views.FilterProductsBySubCategoryAPIView.as_view(),name = 'filter_subcategory'),
    # Related Products
    path('related/products/<slug:slug_product>/',views.RelatedProductAPIView.as_view(),name = 'related_products'),
    # Blogs
    path('blogs/',views.BlogsAPIView.as_view(),name = 'blogs'),
    path('blog/<slug:slug_blog>/',views.RetrieveBlogAPIView.as_view(),name ='blog'),
    # Cart
    path('cart/',views.CartAPIView.as_view(),name = 'cart'),
    path('add/cart/<int:product_id>/',views.AddCartAPIView.as_view(),name ='add_cart'),
    path('remove/cart/<int:product_id>/',views.RemoveCartAPIView.as_view(),name ='remove_cart'),
    path('clear/cart/',views.ClearCartAPIView.as_view(),name = 'clear_cart'),
]
