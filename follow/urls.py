from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views  # Import the views module
from .views import *  
urlpatterns = [
  
    path('followers/', Follow_ListCreateAPIView.as_view()),
    path('followers/<int:pk>/', Follow_DestroyAPIView.as_view()),


]
