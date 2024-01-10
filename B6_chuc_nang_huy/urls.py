from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views  # Import the views module
from .views import *  
urlpatterns = [
    # =====================CHATS========================================
    path('send-message/', SendMessageView.as_view(), name='send-message'),
    # path('send-message/<int:message_id>/', SendMessageView.as_view(), name='send_message_detail'),
    # path('list-user-messages/', views.List_User_Messages, name='List_User_Messages'),
    path('delete_conversation/', views.delete_conversation, name='delete_conversation'),

    # path('follow-user/',views.follow_member),
    # path('list-user-follow/',views.list_follow_member),
    # path('list-user-followed/',views.list_followed_member),
    # path('delete-follow/',views.delete_follow_member),
    # path('list-user-un-follow/',views.list_unfollow_member),

    # path('review-view/',ReviewView.as_view()),
    path('messger/', Send_Message_ListCreateAPIView.as_view()),
    # path('messger/<int:pk>/', Send_Message_RetrieveUpdateDestroyAPIView.as_view()),
    path('follow/', Follow_ListCreateAPIView.as_view()),
    path('follow/<int:pk>/', Follow_RetrieveUpdateDestroyAPIView.as_view()),
    path('review/',ReviewView_ListCreateAPIView.as_view()),
    path('review/<int:pk>/', ReviewView_RetrieveUpdateDestroyAPIView.as_view()),
    

]
