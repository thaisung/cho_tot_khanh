# tooicaif/urls.py

from django.urls import path
from .views import *  

urlpatterns = [
    # path('category/', Category_ListCreateAPIView.as_view(), name='category-list-create'),
    # path('category/<int:pk>/', Category_RetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('users/', User_ListCreateView.as_view()),
    path('users/<int:pk>/', User_RetrieveUpdateDeleteView.as_view()),
    
    path('location/', Location_ListCreateAPIView.as_view()),
    path('location/<int:pk>/', Location_RetrieveUpdateDestroyAPIView.as_view()),

    path('location/address/', Address_ListCreateAPIView.as_view()),
    path('location/address/<int:pk>/', Address_RetrieveUpdateDestroyAPIView.as_view()),


]