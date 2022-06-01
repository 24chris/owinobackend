import imp
from django.urls import path, include
from .views import ProductDetail

from product import views

urlpatterns = [
    path('latest-products/',views.LatestProductsList.as_view()),
    # path('flash/',views.FlashProductsList.as_view()),
    # path('trend/',views.TrendProductsList.as_view()),
    # path('women/',views.WomenProductsList.as_view()),
    # path('discount/',views.DiscountProductsList.as_view()),
    path('products/search',views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/',views.CategoryDetail.as_view()),
    
]