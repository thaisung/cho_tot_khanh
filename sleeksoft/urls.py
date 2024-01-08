"""sleeksoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenBlacklistView
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from chotot.views import *
from django.conf.urls.static import static

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
    # path('/', admin.site.urls),
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', CustomTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/blacklist/', TokenBlacklistView.as_view()),
    path('api/user-information/',get_user_info),
    
    path('', include('chotot.urls')),
    # path('auth/', include('social_django.urls', namespace='social')),
    # A1
    path('job/', include('A1_viec_lam.urls')),
    # end A1
    # A2
    path('good-house/', include('A2_nha_tot.urls')),
    # end A2
    # A3
    path('refrigerator-airconditioner-washingmachine/', include('A3_tu_lanh_may_lanh_may_giat.urls')),
    # end A3
    # A4
    path('machinery-equipment/', include('A4_may_moc_thiet_bi_chuyen_dung.urls')),
    # end A4
    # A5
    path('taxi/', include('A5_taxi.urls')),
    # end A5
    # all
    # path('all/', include('all.urls')),
    # end all
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
