from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views  # Import the views module
from .views import *  
urlpatterns = [

    path('review_user/',ReviewView_ListCreateAPIView.as_view()),
    path('review_user/<int:pk>/', ReviewView_RetrieveUpdateDestroyAPIView.as_view()),


    

]
