from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 401:
        # Xử lý lỗi xác thực 401 ở đây
        response.data = {
            'status': status.HTTP_401_UNAUTHORIZED,
            'error_message': 'Thông tin xác thực không chính xác',
        }

    return response