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
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import authentication_classes, permission_classes

import os

class IsAdminOrAssociatedUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Cho phép admin truy cập tất cả
        if request.user.is_staff:
            return True
        # Cho phép người dùng liên quan truy cập
        return obj.user == request.user

class Posted_news_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Posted_news.objects.all()
    serializer_class = Posted_news_Serializer
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
        
class Posted_news_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posted_news.objects.all()
    serializer_class = Posted_news_Serializer
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

class Poster_information_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Poster_information.objects.all()
    serializer_class = Poster_information_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','Name']
    search_fields = ['id','Name']
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
class Poster_information_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poster_information.objects.all()
    serializer_class = Poster_information_Serializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method in ['PUT','PATCH','DELETE']:
            return [IsAuthenticated(), IsAdminUser()]
        
class Items_Pagination(PageNumberPagination):
    page_size = 10  # Số lượng bản ghi trên mỗi trang
    page_size_query_param = 'page_size'
    max_page_size = 100
class Items_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = Items_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','User__username','Map','Price','Posted_news__Name','Place_of_origin','Destination','Time_to_start_moving','Title','Detailed_description','Poster_information__Name']
    search_fields = ['id','User__username','Map','Price','Posted_news__Name','Place_of_origin','Destination','Time_to_start_moving','Title','Detailed_description','Poster_information__Name']
    pagination_class = Items_Pagination
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = {'status': status.HTTP_200_OK, 'message': 'Get the list of Users successfully', 'data': response.data}
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        print('request.data:', request.data)
        images_A5_data = request.data.pop('images_A5_data', [])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Trích xuất các giá trị ID từ request.data
            posted_news_id = request.data.get('Posted_news')
            poster_information_id = request.data.get('Poster_information')

            # Lấy bản ghi từ cơ sở dữ liệu
            posted_news = Posted_news.objects.get(pk=posted_news_id)
            poster_information = Poster_information.objects.get(pk=poster_information_id)

            # Tạo instance của Job với các giá trị đã lấy được
            item_instance = serializer.save(User=request.user,
                                            Posted_news=posted_news,Poster_information=poster_information
                                            )

            for image_data in images_A5_data:
                Items_image.objects.create(Items=item_instance, Image=image_data)

            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            print('serializer.errors:', serializer.errors)
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
class Items_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = Items_Serializer
    def get_permissions(self):
        if self.request.method in ['GET','PUT','PATCH','DELETE']:
            return [IsAuthenticated(),IsAdminOrAssociatedUser()]
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
        # Kiểm tra xem có dữ liệu mới ảnh và video được nhập hay không
        has_new_images = 'images_A5_data' in request.data and request.data['images_A5_data']
        has_new_video = 'Video' in request.data and request.data['Video']
        # Kiểm tra và xóa ảnh cũ nếu có dữ liệu mới
        if has_new_images:
            old_images = Items_image.objects.filter(Items=instance)
            print('old_images:',old_images)
            for i in old_images:
                os.remove(i.Image.path)
            old_images.delete()
            images_A5_data = request.data.pop('images_A5_data', [])
            for image_data in images_A5_data:
                    Items_image.objects.create(Items=instance, Image=image_data)
        # Kiểm tra và xóa video cũ nếu có dữ liệu mới
        if has_new_video and instance.Video.path:
            print('instance.Video.path:',instance.Video.path)
            os.remove(instance.Video.path)
        # Cập nhật thông tin
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save(User=request.user)
            data = {'status': status.HTTP_200_OK, 'message': 'Update successful', 'data': serializer.data}
            return Response(data, status=status.HTTP_200_OK)
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

class Items_image_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Items_image.objects.all()
    serializer_class = Items_image_Serializer
class Items_image_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items_image.objects.all()
    serializer_class = Items_image_Serializer
