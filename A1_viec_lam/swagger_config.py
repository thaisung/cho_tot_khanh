# Trong file swagger_config.py của mỗi app
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi

INFO = openapi.Info(
    title=_("Việc làm"),
    default_version='v1',
    description=_("Mô tả của app"),
    terms_of_service=_("Điều khoản sử dụng"),
    contact=openapi.Contact(email="contact@app.com"),
    license=openapi.License(name=_("Giấy phép của app")),
)
