# tooicaif/urls.py

from django.urls import path
from .views import *  

urlpatterns = [
    path('posted-news/', Posted_news_ListCreateAPIView.as_view()),
    path('posted-news/<int:pk>/', Posted_news_RetrieveUpdateDestroyAPIView.as_view()),

    path('poster-information/', Poster_information_ListCreateAPIView.as_view()),
    path('poster-information/<int:pk>/', Poster_information_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/',Items_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Items_RetrieveUpdateDestroyAPIView.as_view()),

    # path('items-image/', Items_image_ListCreateAPIView.as_view()),
    # path('items-image/<int:pk>/', Items_image_RetrieveUpdateDestroyAPIView.as_view()),
]
