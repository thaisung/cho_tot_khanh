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
# Create your views here.

class Follow_ListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    # queryset = Follow.objects.all()
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_queryset(self):
        logged_in_user = self.request.user.id  # Sử dụng user hiện tại
        queryset = Follow.objects.filter(Q(followers=logged_in_user) | Q(watching=logged_in_user))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # serializer = self.get_serializer(queryset, many=True)
        serializer = FollowSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = FollowSerializer(data=request.data)  # Pass the request data to the serializer
        if serializer.is_valid():
            user_watching = request.data.get('watching')
            followers = request.user
            # breakpoint()
            watching = User.objects.get(pk=user_watching)
            # followers = User.objects.get(pk=followers)

            serializer.validated_data['watching'] = watching
            serializer.validated_data['followers'] = followers

            # content = f"{follower.username} đã theo dõi bạn."
            # Notification.objects.create(user=userr, user_send=follower, content=content)
            # Gửi thông báo qua email
            # subject = 'Bạn có một thông báo mới'
            # message = content
            # # from_email = 'quanghuyqb2001@gmial.com'  # Điền địa chỉ email của bạn
            # from_email = f'khanh skyshop'

            # recipient_list = [userr.email]

            # send_mail(subject, message, from_email, recipient_list)

            serializer.save()
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class Follow_DestroyAPIView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        
        try:
            # Lấy id của tin nhắn từ đối số URL
            Follow_id = self.kwargs.get('pk')
            
            # Kiểm tra xem tin nhắn có tồn tại không
            follow = get_object_or_404(Follow, id=Follow_id)
            if request.user == follow.followers :
                # Xóa tin nhắn
                follow.delete()

                return Response({'status': status.HTTP_204_NO_CONTENT, 'message': 'Bỏ theo dõi thành công'})
            else:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': ' Bạn Không có quyền xóa bỏ theo dõi'})
        except Exception as e:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Lỗi: {}'.format(str(e))})