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

    path('companies/', Company_ListCreateAPIView.as_view()),
    path('companies/<int:pk>/', Company_RetrieveUpdateDestroyAPIView.as_view()),

    path('years-of-manufacture/', Year_of_manufacture_ListCreateAPIView.as_view()),
    path('years-of-manufacture/<int:pk>/', Year_of_manufacture_RetrieveUpdateDestroyAPIView.as_view()),

    path('gearboxes/', Gearbox_ListCreateAPIView.as_view()),
    path('gearboxes/<int:pk>/', Gearbox_RetrieveUpdateDestroyAPIView.as_view()),

    path('fuels/', Fuel_ListCreateAPIView.as_view()),
    path('fuels/<int:pk>/', Fuel_RetrieveUpdateDestroyAPIView.as_view()),

    path('seat-numbers/', Seat_number_ListCreateAPIView.as_view()),
    path('seat-numbers/<int:pk>/', Seat_number_RetrieveUpdateDestroyAPIView.as_view()),

    path('capacities/', Capacity_ListCreateAPIView.as_view()),
    path('capacities/<int:pk>/', Capacity_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/',Items_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Items_RetrieveUpdateDestroyAPIView.as_view()),

    path('items-image/', Items_image_ListCreateAPIView.as_view()),
    path('items-image/<int:pk>/', Items_image_RetrieveUpdateDestroyAPIView.as_view()),
]
