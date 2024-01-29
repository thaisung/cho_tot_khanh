from django.conf import settings
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission
import jwt
from rest_framework.pagination import PageNumberPagination
from chotot.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import authentication_classes, permission_classes
from chotot.serializers import *
from django.core.mail import send_mail
from operator import attrgetter


class ReviewView_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        logged_in_user = self.request.user.id  # Sử dụng user hiện tại
        queryset = Review.objects.filter(user_seller=logged_in_user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # serializer = self.get_serializer(queryset, many=True)
        serializer = ReviewSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)  # Pass the request data to the serializer
        if serializer.is_valid():
            # user_id = request.data.get('user')
            user_seller_id = request.data.get('user_seller')
            # breakpoint()
            # user = User.objects.get(pk=user_id)
            user = request.user
            user_seller = User.objects.get(pk=user_seller_id)
            check = Review.objects.filter(Q(user=user) and Q(user_seller=user_seller))
            if check:
                data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Bạn chỉ đánh giá được 1 lần', 'error': serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data['user'] = user
            serializer.validated_data['user_seller'] = user_seller
            
            rating = request.data.get('rating')
            sao = int(rating)
            if not (1 <= sao <= 5):
                data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Đánh giá không hợp lệ. Đánh giá phải nằm trong khoảng từ 1 đến 5 sao.'}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            serializer.validated_data['rating'] = sao

            serializer.save()
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class ReviewView_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
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