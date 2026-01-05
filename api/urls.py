from django.urls import path
from .views import CategoryListAPIView, ProductListAPIView, HomeDataAPIView, ContactMessageCreateAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('home/', HomeDataAPIView.as_view(), name='home-data'),
    path('contact/', ContactMessageCreateAPIView.as_view(), name='contact-message-create'),
]