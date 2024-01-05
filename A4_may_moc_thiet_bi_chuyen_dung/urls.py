# tooicaif/urls.py

from django.urls import path
from .views import *  

urlpatterns = [
    path('usage-status/', Usage_status_ListCreateAPIView.as_view()),
    path('usage-status/<int:pk>/', Usage_status_RetrieveUpdateDestroyAPIView.as_view()),

    path('seller-information/', Seller_information_ListCreateAPIView.as_view()),
    path('seller-information/<int:pk>/', Seller_information_RetrieveUpdateDestroyAPIView.as_view()),

    path('guarantee/', Guarantee_ListCreateAPIView.as_view()),
    path('guarantee/<int:pk>/', Guarantee_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/',Items_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Items_RetrieveUpdateDestroyAPIView.as_view()),

    # path('items-image/', Items_image_ListCreateAPIView.as_view()),
    # path('items-image/<int:pk>/', Items_image_RetrieveUpdateDestroyAPIView.as_view()),
]
