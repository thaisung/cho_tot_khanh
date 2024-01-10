from django.urls import path
from .views import *  

urlpatterns = [
    
    path('category/', Category_ListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', Category_RetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),


    path('seller-information/', Seller_information_ListCreateAPIView.as_view()),
    path('seller-information/<int:pk>/', Seller_information_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/',Items_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Items_RetrieveUpdateDestroyAPIView.as_view()),

    path('items-image/', Items_image_ListCreateAPIView.as_view()),
    path('items-image/<int:pk>/', Items_image_RetrieveUpdateDestroyAPIView.as_view()),
]
