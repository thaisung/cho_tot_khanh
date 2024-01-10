from django.urls import path
from .views import *  

urlpatterns = [
    
    path('category/', Category_ListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', Category_RetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('usage-status/', Usage_status_ListCreateAPIView.as_view()),
    path('usage-status/<int:pk>/', Usage_status_RetrieveUpdateDestroyAPIView.as_view()),

    path('seller-information/', Seller_information_ListCreateAPIView.as_view()),
    path('seller-information/<int:pk>/', Seller_information_RetrieveUpdateDestroyAPIView.as_view()),

    path('companies/', Company_ListCreateAPIView.as_view()),
    path('companies/<int:pk>/', Company_RetrieveUpdateDestroyAPIView.as_view()),

    path('color/', Color_ListCreateAPIView.as_view()),
    path('color/<int:pk>/', Color_RetrieveUpdateDestroyAPIView.as_view()),

    path('capacities/', Capacity_ListCreateAPIView.as_view()),
    path('capacities/<int:pk>/', Capacity_RetrieveUpdateDestroyAPIView.as_view()),

    path('guarantee/', Guarantee_ListCreateAPIView.as_view()),
    path('guarantee/<int:pk>/', Guarantee_RetrieveUpdateDestroyAPIView.as_view()),

    path('microprocessor/', Microprocessor_ListCreateAPIView.as_view()),
    path('microprocessor/<int:pk>/', Microprocessor_RetrieveUpdateDestroyAPIView.as_view()),

    path('ram/', Ram_ListCreateAPIView.as_view()),
    path('ram/<int:pk>/', Ram_RetrieveUpdateDestroyAPIView.as_view()),

    path('hard_drive/', Hard_drive_ListCreateAPIView.as_view()),
    path('hard_drive/<int:pk>/', Hard_drive_RetrieveUpdateDestroyAPIView.as_view()),

    path('monitor_card/', Monitor_card_ListCreateAPIView.as_view()),
    path('monitor_card/<int:pk>/', Monitor_card_RetrieveUpdateDestroyAPIView.as_view()),

    path('screen_size/', Screen_size_ListCreateAPIView.as_view()),
    path('screen_size/<int:pk>/', Screen_size_RetrieveUpdateDestroyAPIView.as_view()),


    path('items/',Items_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Items_RetrieveUpdateDestroyAPIView.as_view()),

    path('items-image/', Items_image_ListCreateAPIView.as_view()),
    path('items-image/<int:pk>/', Items_image_RetrieveUpdateDestroyAPIView.as_view()),
]
