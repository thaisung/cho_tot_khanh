from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views  # Import the views module
from .views import *  
urlpatterns = [


    path('notification/',Notification_ListCreateAPIView.as_view()),
    path('notification/<int:pk>/',Notification_RetrieveUpdateDestroyAPIView.as_view()),

   
    

]
