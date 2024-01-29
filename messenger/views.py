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
from rest_framework import permissions

# Create your views here.
class IsMessageOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kiểm tra xem người thực hiện yêu cầu có phải là chủ sở hữu của tin nhắn không
        return obj.sender == request.user or obj.receiver == request.user

class Message_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        logged_in_user = self.request.user
        messenger_user = Message.objects.filter(
            Q(sender=logged_in_user) & Q(sender_deleted=False) |
            Q(receiver=logged_in_user) & Q(receiver_deleted=False)
        )
        return messenger_user

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Lấy ra danh sách người dùng liên quan đến tin nhắn
        related_users = set()
        for message in queryset:
            related_users.add(message.sender)
            related_users.add(message.receiver)

        # Loại bỏ người dùng hiện tại khỏi danh sách
        related_users.discard(request.user)
        # Tạo một danh sách người dùng và tin nhắn được serialize
        user_messages_list = []
        for user in related_users:
            user_messages_dict = {
                'user': User_Serializer(user).data,
                'product':[],
                'messages': []
            }

            # Lọc ra những tin nhắn liên quan đến user trong vòng lặp
            user_messages = queryset.filter(
                Q(sender=user, receiver=request.user) |
                Q(sender=request.user, receiver=user)
            ).order_by('-timestamp')

            latest_message = user_messages.first()

            user_messages_dict['product'].append({
                'id_products': latest_message.id_products,
                'url_parent': latest_message.url_parent,
            })
            for message in user_messages:
                user_messages_dict['messages'].append({
                    'id': message.id,
                    'content': message.content,
                    'timestamp': message.timestamp,
                    'sender': User_Serializer(message.sender).data['username'],
                    'receiver': User_Serializer(message.receiver).data['username']
                })
                

            user_messages_list.append(user_messages_dict)
        # Sắp xếp danh sách theo thời gian tin nhắn cuối cùng giảm dần
        user_messages_list = sorted(user_messages_list, key=lambda x: x['messages'][0]['timestamp'], reverse=True)
        
        data = {
            'status': status.HTTP_200_OK,
            'message': 'Lấy danh sách người dùng thành công',
            'data': user_messages_list
        }

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            sender_id = request.data.get('sender')
            sender = User.objects.get(pk=sender_id)

            receiver_id = request.data.get('receiver')
            receiver = User.objects.get(pk=receiver_id)

            # Set the sender and receiver fields before saving
            serializer.validated_data['sender'] = sender
            serializer.validated_data['receiver'] = receiver

            # Save the instance with the modified data
            serializer.save()

            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Message sent successfully',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Message creation failed',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class MessageDestroyAllAPIView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsMessageOwner]
    def destroy(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            other_user_id = self.kwargs.get('other_user_id')

            # Kiểm tra xem cả hai user_id có tồn tại không
            user = get_object_or_404(User, id=user_id)
            other_user = get_object_or_404(User, id=other_user_id)

            # Đặt trạng thái xóa cho người gửi
            Message.objects.filter(sender=user, receiver=other_user).update(sender_deleted=True)

            # Đặt trạng thái xóa cho người nhận
            Message.objects.filter(sender=other_user, receiver=user).update(receiver_deleted=True)

            return Response({'status': status.HTTP_200_OK, 'message': 'Cuộc hội thoại đã được đánh dấu là đã xóa thành công'})

        except Exception as e:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Lỗi: {}'.format(str(e))})

class MessageDestroyAPIView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsMessageOwner]

    def destroy(self, request, *args, **kwargs):
        try:
            # Lấy id của tin nhắn từ đối số URL
            message_id = self.kwargs.get('pk')
            
            # Kiểm tra xem tin nhắn có tồn tại không
            message = get_object_or_404(Message, id=message_id)
            if request.user == message.sender or  request.user == message.receiver :
                # Xóa tin nhắn
                message.delete()

                return Response({'status': status.HTTP_204_NO_CONTENT, 'message': 'Xóa tin nhắn thành công'})
            else:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': ' Bạn Không có quyền xóa tin nhắn'})
        except Exception as e:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Lỗi: {}'.format(str(e))})