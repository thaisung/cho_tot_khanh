# tooicaif/urls.py

from django.urls import path
from .views import * 

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from .swagger_config import INFO
# from .swagger_config import INFO
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Chợ tốt API",
        default_version='v1',
        description="6 mục API Chợ tốt ThaiPT",
        terms_of_service="http://127.0.0.1:8000/",
        contact=openapi.Contact(email="vuthaind@gmail.com"),
        license=openapi.License(name="ko có"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('career/', Career_ListCreateAPIView.as_view(), name='Career-list-create'),
    path('career/<int:pk>/', Career_RetrieveUpdateDestroyAPIView.as_view(), name='Career-retrieve-update-destroy'),

    path('type-of-work/',Type_of_work_ListCreateAPIView.as_view()),
    path('type-of-work/<int:pk>/', Type_of_work_RetrieveUpdateDestroyAPIView.as_view()),

    path('pay-forms/', Pay_forms_ListCreateAPIView.as_view()),
    path('pay-forms/<int:pk>/', Pay_forms_RetrieveUpdateDestroyAPIView.as_view()),

    path('sex/', Sex_ListCreateAPIView.as_view()),
    path('sex/<int:pk>/',Sex_RetrieveUpdateDestroyAPIView.as_view()),

    path('experience/', Experience_ListCreateAPIView.as_view()),
    path('experience/<int:pk>/', Experience_RetrieveUpdateDestroyAPIView.as_view()),

    path('items/', Job_ListCreateAPIView.as_view()),
    path('items/<int:pk>/', Job_RetrieveUpdateDestroyAPIView.as_view()),

    path('items-image/', Job_image_ListCreateAPIView.as_view()),
    path('items-image/<int:pk>/', Job_image_RetrieveUpdateDestroyAPIView.as_view()),

    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
