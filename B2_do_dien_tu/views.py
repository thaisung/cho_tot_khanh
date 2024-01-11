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
# from chotot.models import *

import os

class IsAdminOrAssociatedUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Cho phép admin truy cập tất cả
        if request.user.is_staff:
            return True
        # Cho phép người dùng liên quan truy cập
        return obj.user == request.user

class Category_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = B2CategorySerializer
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

            # location_id = request.data.get('ParentCategory')
              
            # ParentCatego = ParentCategory.objects.get(pk=location_id)
            # # breakpoint()
            # item_instance = serializer.save(ParentCategory=ParentCatego)
            
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST,'message':'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
class Category_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = B2CategorySerializer
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

class Usage_status_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Usage_status.objects.all()
    serializer_class = B2UsageStatusSerializer
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

class Usage_status_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usage_status.objects.all()
    serializer_class = B2UsageStatusSerializer
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

class Company_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = B2CompanySerializer
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
class Company_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = B2CompanySerializer
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


class Color_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = B2ColorSerializer
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
class Color_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = B2ColorSerializer
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

class Capacity_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Capacity.objects.all()
    serializer_class = B2CapacitySerializer
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

class Capacity_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capacity.objects.all()
    serializer_class = B2CapacitySerializer
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

class Guarantee_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Guarantee.objects.all()
    serializer_class = B2GuaranteeSerializer
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
class Guarantee_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guarantee.objects.all()
    serializer_class = B2GuaranteeSerializer
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

class Microprocessor_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Microprocessor.objects.all()
    serializer_class = B2MicroprocessorSerializer
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
class Microprocessor_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Microprocessor.objects.all()
    serializer_class = B2MicroprocessorSerializer
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

class Ram_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ram.objects.all()
    serializer_class = B2RamSerializer
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

class Ram_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ram.objects.all()
    serializer_class = B2RamSerializer
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

class Hard_drive_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hard_drive.objects.all()
    serializer_class = B2HardDriveSerializer
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
class Hard_drive_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hard_drive.objects.all()
    serializer_class = B2HardDriveSerializer
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

class Monitor_card_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Monitor_card.objects.all()
    serializer_class = B2MonitorCardSerializer
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
class Monitor_card_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monitor_card.objects.all()
    serializer_class = B2MonitorCardSerializer
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

class Screen_size_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Screen_size.objects.all()
    serializer_class = B2ScreenSizeSerializer
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

class Screen_size_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screen_size.objects.all()
    serializer_class = B2ScreenSizeSerializer
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

class Seller_information_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seller_information.objects.all()
    serializer_class = B2SellerInformationSerializer
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
class Seller_information_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller_information.objects.all()
    serializer_class = B2SellerInformationSerializer
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

class Items_Pagination(PageNumberPagination):
    page_size = 2  # Số lượng bản ghi trên mỗi trang
    page_size_query_param = 'page_size'
    max_page_size = 100

class Items_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = B2Items_Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','User__username','Map','Location__Name','Address__Name','Category__Name','Usage_status__Name',
                        'Guarantee__Name','Company__Name','Color__Name','Capacity__Name','Microprocessor__Name','Ram__Name','Hard_drive__Name',
                        'Monitor_card__Name','Screen_size__Name','Seller_information__Name','Free_giveaway','Price','Title','Detailed_description']

    search_fields = ['id','User__username','Map','Location__Name','Address__Name','Category__Name','Usage_status__Name',
                        'Guarantee__Name','Company__Name','Color__Name','Capacity__Name','Microprocessor__Name','Ram__Name','Hard_drive__Name',
                        'Monitor_card__Name','Screen_size__Name','Seller_information__Name','Free_giveaway','Price','Title','Detailed_description']

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
        images_A3_data = request.data.pop('images_A3_data', [])
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Trích xuất các giá trị ID từ request.data
            location_id = request.data.get('Location')
            location = Location.objects.get(pk=location_id)

            address_id = request.data.get('Address')
            address = Address.objects.get(pk=address_id)

            category_id = request.data.get('Category')
            category = Category.objects.get(pk=category_id)

            usage_status_id = request.data.get('Usage_status')
            usage_status = Usage_status.objects.get(pk=usage_status_id)

            seller_information_id = request.data.get('Seller_information')
            seller_information = Seller_information.objects.get(pk=seller_information_id)

            guarantee_id = request.data.get('Guarantee')
            guarantee = Guarantee.objects.get(pk=guarantee_id)

            company_id = request.data.get('Company')
            company = Company.objects.get(pk=company_id) if company_id else None

            color_id = request.data.get('Color')
            color = Color.objects.get(pk=color_id) if color_id else None

            capacity_id = request.data.get('Capacity')
            capacity = Capacity.objects.get(pk=capacity_id) if capacity_id else None

            microprocessor_id = request.data.get('Microprocessor')
            microprocessor = Microprocessor.objects.get(pk=microprocessor_id) if microprocessor_id else None

            ram_id = request.data.get('Ram')
            ram = Ram.objects.get(pk=ram_id) if ram_id else None

            hard_drive_id = request.data.get('Hard_drive')
            hard_drive = Hard_drive.objects.get(pk=hard_drive_id) if hard_drive_id else None

            monitor_card_id = request.data.get('Monitor_card')
            monitor_card = Monitor_card.objects.get(pk=monitor_card_id) if monitor_card_id else None

            screen_size_id = request.data.get('Screen_size')
            screen_size = Screen_size.objects.get(pk=screen_size_id) if screen_size_id else None

            
            # Tạo instance của Job với các giá trị đã lấy được
            item_instance = serializer.save(User=request.user, Location=location, Address=address,
                                            Category=category,Usage_status=usage_status,Seller_information=seller_information,
                                            Guarantee=guarantee,Company=company,Color=color,Capacity=capacity,
                                            Microprocessor=microprocessor,Ram=ram,Hard_drive=hard_drive,Monitor_card=monitor_card,
                                            Screen_size=screen_size)

            for image_data in images_A3_data:
                Items_image.objects.create(Items=item_instance, Image=image_data)

            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class Items_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = B2Items_Serializer
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
        has_new_images = 'images_A3_data' in request.data and request.data['images_A3_data']
        has_new_video = 'Video' in request.data and request.data['Video']
        # Kiểm tra và xóa ảnh cũ nếu có dữ liệu mới
        if has_new_images:
            old_images = Items_image.objects.filter(Items=instance)
            for i in old_images:
                os.remove(i.Image.path)
            old_images.delete()
            images_A3_data = request.data.pop('images_A3_data', [])
            for image_data in images_A3_data:
                    Items_image.objects.create(Items=instance, Image=image_data)
        # Kiểm tra và xóa video cũ nếu có dữ liệu mới
        if has_new_video and instance.Video.path:
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
    serializer_class = B2Items_image_Serializer
class Items_image_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items_image.objects.all()
    serializer_class = B2Items_image_Serializer