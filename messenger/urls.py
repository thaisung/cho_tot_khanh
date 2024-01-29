from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views  # Import the views module
from .views import *  
urlpatterns = [
    # =====================CHATS========================================
    path('send_Messenger/', Message_ListCreateAPIView.as_view()),
    # path('send_Messenger/<int:pk>/', Message_RetrieveUpdateDestroyAPIView.as_view()),
    path('send_Messenger/<int:pk>/', MessageDestroyAPIView.as_view(), name='delete_message'),
    path('send_Messenger/delete_all/<int:other_user_id>/', MessageDestroyAllAPIView.as_view(), name='delete_all_messages'),

    

]
