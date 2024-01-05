from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except PermissionDenied:
            # Xử lý lỗi 401 tùy chỉnh
            data = {'error_message': 'Thông tin xác thực không chính xác.'}
            response = Response(data, status=status.HTTP_401_UNAUTHORIZED)

        return response
