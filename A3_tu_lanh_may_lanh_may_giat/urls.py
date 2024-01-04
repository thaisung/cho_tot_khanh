# tooicaif/urls.py

from django.urls import path
from .views import *  

urlpatterns = [
    path('category/', Category_ListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', Category_RetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('usage-status/', Usage_status_ListCreateAPIView.as_view()),
    path('usage-status/<int:pk>/', Usage_status_RetrieveUpdateDestroyAPIView.as_view()),

    path('seller-information/', Seller_information_ListCreateAPIView.as_view()),
    path('seller-information/<int:pk>/', Seller_information_RetrieveUpdateDestroyAPIView.as_view()),

    path('guarantee/', Guarantee_ListCreateAPIView.as_view()),
    path('guarantee/<int:pk>/', Guarantee_RetrieveUpdateDestroyAPIView.as_view()),

    path('volume/', Volume_ListCreateAPIView.as_view()),
    path('volume/<int:pk>/', Volume_RetrieveUpdateDestroyAPIView.as_view()),

    path('wattage/', Wattage_ListCreateAPIView.as_view()),
    path('wattage/<int:pk>/', Wattage_RetrieveUpdateDestroyAPIView.as_view()),

    path('washing-volume/', Washing_volume_ListCreateAPIView.as_view()),
    path('washing-volume/<int:pk>/', Washing_volume_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/',Items_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Items_RetrieveUpdateDestroyAPIView.as_view()),

    path('items-image/', Items_image_ListCreateAPIView.as_view()),
    path('items-image/<int:pk>/', Items_image_RetrieveUpdateDestroyAPIView.as_view()),
]
