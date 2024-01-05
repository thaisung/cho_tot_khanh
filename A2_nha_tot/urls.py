# tooicaif/urls.py

from django.urls import path
from .views import *  

urlpatterns = [
    path('category/', Category_ListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', Category_RetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('interior-condition/', Interior_condition_ListCreateAPIView.as_view()),
    path('interior-condition/<int:pk>/', Interior_condition_RetrieveUpdateDestroyAPIView.as_view()),

    path('seller-information/', Seller_information_ListCreateAPIView.as_view()),
    path('seller-information/<int:pk>/', Seller_information_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/', Products_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Products_RetrieveUpdateDestroyAPIView.as_view()),

    # path('products-image/', Products_image_ListCreateAPIView.as_view()),
    # path('products-image/<int:pk>/', Products_image_RetrieveUpdateDestroyAPIView.as_view()),

]
