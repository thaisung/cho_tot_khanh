from .models import *
from .serializers import *
from rest_framework import generics
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics,filters

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView,RetrieveAPIView

from B1_xe_co.models import *
from B1_xe_co.serializers import *

from B2_do_dien_tu.models import *
from B2_do_dien_tu.serializers import *

from B3_dich_vu.models import *
from B3_dich_vu.serializers import *

from B4_do_gia_dung_noi_that.models import *
from B4_do_gia_dung_noi_that.serializers import *

from B5_cua_hang_viet.models import *
from B5_cua_hang_viet.serializers import *

from A1_viec_lam.models import Job as ItemsA1
from A1_viec_lam.serializers import Job_Serializer as A1Items_Serializer

from A2_nha_tot.models import Products as ItemsA2
from A2_nha_tot.serializers import Products_Serializer as A2Items_Serializer

from A3_tu_lanh_may_lanh_may_giat.models import Items as ItemsA3
from A3_tu_lanh_may_lanh_may_giat.serializers import Items_Serializer as A3Items_Serializer

from A4_may_moc_thiet_bi_chuyen_dung.models import Items as ItemsA4
from A4_may_moc_thiet_bi_chuyen_dung.serializers import Items_Serializer as A4Items_Serializer

from A5_taxi.models import Items as ItemsA5
from A5_taxi.serializers import Items_Serializer as A5Items_Serializer


from operator import attrgetter

@api_view(['GET'])
def get_user_info(request):
    try:
        # Kiểm tra xác thực bằng token
        if not request.auth or not IsAuthenticated().has_permission(request, None):
            raise AuthenticationFailed(detail='Thông tin xác thực không chính xác', code='token_not_valid')

        # Logic của view
        user = User_Serializer(request.user).data
        data = {'status': status.HTTP_200_OK, 'message': 'Lấy thông tin thành công', 'data': user}
        return Response(data, status=status.HTTP_200_OK)
    except AuthenticationFailed as e:
        # Xử lý lỗi xác thực không thành công
        detail = 'Thông tin xác thực không chính xác' if not e.detail else e.detail
        data = {'status': status.HTTP_401_UNAUTHORIZED, 'error_message': detail}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        data = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': 'Lấy thông tin thất bại'}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user  # Thay đổi ở đây
            refresh = response.data['refresh']
            access = response.data['access']
            
            # Thêm thông tin user vào response
            response.data['user'] = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff':user.is_staff
                # Thêm các thông tin user khác nếu cần
            }
            
            # Thêm refresh token và access token vào response
            response.data['refresh'] = refresh
            response.data['access'] = access

        # Sử dụng Response mới để đảm bảo cả thông báo và status code được trả về
        data = {'status': status.HTTP_200_OK, 'message': 'Logged in successfully', 'data': response.data}
        return Response(data, status=status.HTTP_200_OK)

class IsOwnerOrAdminPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kiểm tra xem user có là admin hay không
        is_admin = request.user.is_staff
        print(' is_admin', is_admin)

        # Nếu user là admin, hoặc là chính user trong request, cho phép truy cập
        return is_admin or request.user == obj
    
class User_Pagination(PageNumberPagination):
    page_size = 2  # Số lượng bản ghi trên mỗi trang
    page_size_query_param = 'page_size'
    max_page_size = 100

class User_ListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','registration_type','username','password', 'email','first_name','last_name','is_staff','is_superuser','last_updated','last_login','last_logout','date_joined']
    search_fields = ['id','registration_type','username','password', 'email','first_name','last_name','is_staff','is_superuser','last_updated','last_login','last_logout','date_joined']
    pagination_class = User_Pagination
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(), IsOwnerOrAdminPermission()]
        elif self.request.method == 'POST':
            return []
    def list(self, request, *args, **kwargs):
        is_admin = request.user.is_staff
        print(' is_admin', is_admin)
        print(' is_admin', request.user)
        response = super().list(request, *args, **kwargs)
        data = {'status': status.HTTP_200_OK, 'message': 'Get the list of Users successfully', 'data': response.data}
        return Response(data, status=status.HTTP_200_OK)
    # @authentication_classes([])
    def create(self, request, *args, **kwargs):
        print(' is_admin', request.user)
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(registration_type='JWT')
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST,'message':'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class User_RetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer
    def get_permissions(self):
        if self.request.method in ['GET','PUT','PATCH','DELETE']:
            return [IsAuthenticated(), IsOwnerOrAdminPermission()]
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = {'status': status.HTTP_200_OK, 'message': 'Get detailed record successfully', 'data': serializer.data}
            return Response(data)
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'Not Found'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, *args, **kwargs):
        print(f"HTTP Method: {self.request.method}")
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        fields_to_check_user = ['id', 'registration_type', 'username', 'last_updated', 'last_login', 'last_logout', 'date_joined']
        if any(field in request.data for field in fields_to_check_user):
            data = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Update failed',
                    'error': f"Updates are not allowed for fields {', '.join(fields_to_check_user)}"
                }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        is_admin = request.user.is_staff and request.user.is_superuser
        # Nếu không phải admin, loại bỏ is_staff và is_superuser khỏi dữ liệu yêu cầu
        fields_to_check_admin = ['is_staff', 'is_superuser']
        if not is_admin and any(field1 in request.data for field1 in fields_to_check_admin):
            print('đã vào')
            data = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Update failed',
                    'error': f"You are not authorized to update fields {', '.join(fields_to_check_admin)}"
                }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if 'password' in request.data:
            password = request.data.get('password', '')
            # Kiểm tra xem password có giá trị không
            if not password:
                data = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Update failed',
                    'error': {'password': 'Password cannot be empty'}
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            request.data['password'] = make_password(request.data['password'])
        if serializer.is_valid():
            serializer.save()
            data = {'status': status.HTTP_200_OK, 'message': 'Update successful', 'data': serializer.data}
            return Response(data,status=status.HTTP_200_OK)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Update failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            data = {'status': status.HTTP_200_OK, 'message': 'Deleted successfully'}
            return Response(data, status=status.HTTP_200_OK)
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'No content found to delete'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class Location_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = Location_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','Name']
    search_fields = ['id','Name']
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = {'status': status.HTTP_200_OK, 'message': 'Get the list of Users successfully', 'data': response.data}
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST,'message':'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
class Location_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = Location_Serializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAuthenticated(), IsAdminUser()]
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = {'status': status.HTTP_200_OK, 'message': 'Get detailed record successfully', 'data': serializer.data}
            return Response(data)
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'Not Found'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            data = {'status': status.HTTP_200_OK, 'message': 'Update successful', 'data': serializer.data}
            return Response(data,status=status.HTTP_200_OK)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Update failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            data = {'status': status.HTTP_200_OK, 'message': 'Deleted successfully'}
            return Response(data, status=status.HTTP_200_OK)
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'No content found to delete'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

class Address_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class =Address_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','Name','Name_en','Location__Name']
    search_fields = ['id','Name','Name_en','Location__Name']
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = {'status': status.HTTP_200_OK, 'message': 'Get the list of Users successfully', 'data': response.data}
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        try:
            location_id = request.data.get('Location')
            location_instance = Location.objects.get(pk=location_id)
        except Location.DoesNotExist:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Location does not exist'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Location=location_instance)
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
class Address_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = Address_Serializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAuthenticated(), IsAdminUser()]
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = {'status': status.HTTP_200_OK, 'message': 'Get detailed record successfully', 'data': serializer.data}
            return Response(data)
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'Not Found'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            data = {'status': status.HTTP_200_OK, 'message': 'Update successful', 'data': serializer.data}
            return Response(data,status=status.HTTP_200_OK)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Update failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            data = {'status': status.HTTP_200_OK, 'message': 'Deleted successfully'}
            return Response(data, status=status.HTTP_200_OK)
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'No content found to delete'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        

# class Home_ListAPIView(ListAPIView):
    # serializer_class = B1Items_Serializer  # Chỉ định lớp serializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['User__username']
    
    # def list(self, request, *args, **kwargs):
    #     models = [ItemsB1, ItemsB2, ItemsB3, ItemsB4, ItemsB5]

    #     data_list = [
    #         self.get_serializer(model.objects.all().order_by('-Creation_time'), many=True).data for model in models
    #     ]

    #     # Kiểm tra xem có dữ liệu trong bất kỳ danh sách nào không
    #     if not any(data_list):
    #         return Response({'status': status.HTTP_204_NO_CONTENT, 'message': 'Not Found'}, status=status.HTTP_204_NO_CONTENT)

    #     # Gộp danh sách các danh sách con
    #     flattened_data = [item for sublist in data_list for item in sublist]

    #     # Kiểm tra xem có dữ liệu trong danh sách gộp không
    #     if not flattened_data:
    #         return Response({'status': status.HTTP_204_NO_CONTENT, 'message': 'Not Found'}, status=status.HTTP_204_NO_CONTENT)

    #     # Sắp xếp danh sách gộp dựa trên 'Creation_time' của phần tử đầu tiên
    #     sorted_data = sorted(flattened_data, key=lambda x: x['Creation_time'], reverse=True)

    #     return Response({'status': status.HTTP_200_OK, 'message': 'successfully', 'data': sorted_data}, status=status.HTTP_200_OK)
def get_serializer_class_for_model(model_class):
    # Thêm logic để ánh xạ model_class với serializer_class tương ứng
    if model_class == ItemsB1:
        return B1Items_Serializer
    elif model_class == ItemsB2:
        return B2Items_Serializer
    elif model_class == ItemsB3:
        return B3Items_Serializer
    elif model_class == ItemsB4:
        return B4Items_Serializer
    elif model_class == ItemsB5:
        return B5Items_Serializer
    elif model_class == ItemsA1:
        return A1Items_Serializer
    elif model_class == ItemsA2:
        return A2Items_Serializer
    elif model_class == ItemsA3:
        return A3Items_Serializer
    elif model_class == ItemsA4:
        return A4Items_Serializer
    elif model_class == ItemsA5:
        return A5Items_Serializer
    else:
        raise ValueError(f"No serializer found for model {model_class}")

class Home_ListAPIView(ListAPIView):

    def list(self, request, *args, **kwargs):
        model_classes = [ItemsB1, ItemsB2, ItemsB3, ItemsB4, ItemsB5,ItemsA1,ItemsA2,ItemsA3,ItemsA4,ItemsA5]
        model_data = []

        for model_class in model_classes:
            queryset = model_class.objects.all().order_by('-Creation_time')
            serializer_class = get_serializer_class_for_model(model_class)
            
            # Truyền context trong khởi tạo serializer
            serializer = serializer_class(queryset, many=True, context={'request': self.request})
            model_data.extend(serializer.data)

        # Kiểm tra xem có dữ liệu trong danh sách không
        if not model_data:
            return Response({'status': status.HTTP_200_OK, 'message': 'successfully', 'data': model_data}, status=status.HTTP_200_OK)

        # Sắp xếp danh sách dựa trên 'Creation_time'
        sorted_data = sorted(model_data, key=lambda x: x.get('Creation_time', 0), reverse=True)

        return Response({'status': status.HTTP_200_OK, 'message': 'successfully', 'data': sorted_data}, status=status.HTTP_200_OK)

class UserArticlesAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        model_classes = [ItemsB1, ItemsB2, ItemsB3, ItemsB4, ItemsB5,ItemsA1,ItemsA2,ItemsA3,ItemsA4,ItemsA5]
        model_data = []

        user_id = kwargs.get('user_id', None)
      
        for model_class in model_classes:
            queryset = model_class.objects.filter(User=user_id).order_by('-Creation_time')
            serializer_class = get_serializer_class_for_model(model_class)
            
            # Truyền context trong khởi tạo serializer
            serializer = serializer_class(queryset, many=True, context={'request': self.request})
            model_data.extend(serializer.data)

        # Kiểm tra xem có dữ liệu trong danh sách không
        if not model_data:
            return Response({'status': status.HTTP_200_OK, 'message': 'successfully', 'data': model_data}, status=status.HTTP_200_OK)

        # Sắp xếp danh sách dựa trên 'Creation_time'
        sorted_data = sorted(model_data, key=lambda x: x.get('Creation_time', 0), reverse=True)

        return Response({'status': status.HTTP_200_OK, 'message': 'successfully', 'data': sorted_data}, status=status.HTTP_200_OK)

class detaileArticlesAPIView(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        try:
            model_classes = [ItemsB1, ItemsB2, ItemsB3, ItemsB4, ItemsB5,ItemsA1,ItemsA2,ItemsA3,ItemsA4,ItemsA5]
            model_data = []

            artice_id = kwargs.get('artice_id', None)
            keyForm = kwargs.get('keyForm', None)

            if not artice_id and keyForm:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)


            for model_class in model_classes:
                queryset = model_class.objects.filter(id = artice_id, Category__keyForm=keyForm )
                serializer_class = get_serializer_class_for_model(model_class)
                
                # Truyền context trong khởi tạo serializer
                serializer = serializer_class(queryset, many=True, context={'request': self.request})
                model_data.extend(serializer.data)

            # Kiểm tra xem có dữ liệu trong danh sách không
            if not model_data:
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'No articles'}, status=status.HTTP_404_NOT_FOUND)

            return Response({'status': status.HTTP_200_OK, 'message': 'successfully', 'data': model_data}, status=status.HTTP_200_OK)
    
        except Http404:
            data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'Not Found'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)

       

# class Parent_Category_ListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ParentCategory.objects.all()
#     serializer_class = ParentCategory_Serializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['id','Name']
#     search_fields = ['id','Name']
#     # def get_permissions(self):
#     #     if self.request.method == 'GET':
#     #         return []
#     #     elif self.request.method == 'POST':
#     #         return [IsAuthenticated(), IsAdminUser()]
#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         data = {'status': status.HTTP_200_OK, 'message': 'Get the list of Users successfully', 'data': response.data}
#         return Response(data, status=status.HTTP_200_OK)
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
#             return Response(data, status=status.HTTP_201_CREATED)
#         else:
#             data = {'status': status.HTTP_400_BAD_REQUEST,'message':'Registration failed', 'error': serializer.errors}
#             return Response(data, status=status.HTTP_400_BAD_REQUEST)

# class Parent_Category_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ParentCategory.objects.all()
#     serializer_class = ParentCategory_Serializer
#     # def get_permissions(self):
#     #     if self.request.method == 'GET':
#     #         return []
#     #     elif self.request.method in ['PUT','PATCH','DELETE']:
#     #         return [IsAuthenticated(), IsAdminUser()]
#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             serializer = self.get_serializer(instance)
#             data = {'status': status.HTTP_200_OK, 'message': 'Get detailed record successfully', 'data': serializer.data}
#             return Response(data)
#         except Http404:
#             data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'Not Found'}
#             return Response(data, status=status.HTTP_404_NOT_FOUND)
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', True)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             data = {'status': status.HTTP_200_OK, 'message': 'Update successful', 'data': serializer.data}
#             return Response(data,status=status.HTTP_200_OK)
#         else:
#             data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Update failed', 'error': serializer.errors}
#             return Response(data, status=status.HTTP_400_BAD_REQUEST)
#     def destroy(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             self.perform_destroy(instance)
#             data = {'status': status.HTTP_200_OK, 'message': 'Deleted successfully'}
#             return Response(data, status=status.HTTP_200_OK)
#         except Http404:
#             data = {'status': status.HTTP_404_NOT_FOUND, 'message': 'No content found to delete'}
#             return Response(data, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def google_oauth(request):
    access_token = request.data["access_token"]
    data = {'status': status.HTTP_200_OK, 'message': 'Đăng nhập thành công', 'data': {'user':'Đang viết api'}}
    return Response(data, status=status.HTTP_200_OK)
    # try:
    #     # Kiểm tra xác thực bằng token
    #     if not request.auth or not IsAuthenticated().has_permission(request, None):
    #         raise AuthenticationFailed(detail='Thông tin xác thực không chính xác', code='token_not_valid')

    #     # Logic của view
    #     access_token = request.data["access_token"]
    #     data = {'status': status.HTTP_200_OK, 'message': 'Đăng nhập thành công', 'data': {'user':'Đang viết api'}}
    #     return Response(data, status=status.HTTP_200_OK)
    # except AuthenticationFailed as e:
    #     # Xử lý lỗi xác thực không thành công
    #     detail = 'Thông tin xác thực không chính xác' if not e.detail else e.detail
    #     data = {'status': status.HTTP_401_UNAUTHORIZED, 'error_message': detail}
    #     return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    # except Exception as e:
    #     data = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': 'Lấy thông tin thất bại'}
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def facebook_oauth(request):
    access_token = request.data["access_token"]
    data = {'status': status.HTTP_200_OK, 'message': 'Đăng nhập thành công', 'data': {'user':'Đang viết api'}}
    return Response(data, status=status.HTTP_200_OK)
    # try:
    #     # Kiểm tra xác thực bằng token
    #     if not request.auth or not IsAuthenticated().has_permission(request, None):
    #         raise AuthenticationFailed(detail='Thông tin xác thực không chính xác', code='token_not_valid')

    #     # Logic của view
    #     access_token = request.data["access_token"]
    #     data = {'status': status.HTTP_200_OK, 'message': 'Đăng nhập thành công', 'data': {'user':'Đang viết api'}}
    #     return Response(data, status=status.HTTP_200_OK)
    # except AuthenticationFailed as e:
    #     # Xử lý lỗi xác thực không thành công
    #     detail = 'Thông tin xác thực không chính xác' if not e.detail else e.detail
    #     data = {'status': status.HTTP_401_UNAUTHORIZED, 'error_message': detail}
    #     return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    # except Exception as e:
    #     data = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': 'Lấy thông tin thất bại'}
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST)