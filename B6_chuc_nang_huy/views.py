
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
#-------------------------- CHỨC NĂNG CHATS --------------------------------------
#gửi tin nhắn

class SendMessageView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    # def post(self, request, *args, **kwargs):
    #     try:
    #         sender_id = request.user.id
    #         receiver_id = request.data.get('receiver_id')
    #         content = request.data.get('content')
            
    #         sender = get_object_or_404(User, pk=sender_id)
    #         receiver = get_object_or_404(User, pk=receiver_id)

    #         if not sender or not receiver:
    #             return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Người dùng không tồn tại', 'data': {}}, status=status.HTTP_404_NOT_FOUND)

    #         message = Message.objects.create(sender=sender, receiver=receiver, content=content)
    #         message.save()

    #         message_data = MessageSerializer(message).data
    #         return Response({'status': status.HTTP_201_CREATED, 'message': 'Thành công', 'data': message_data}, status=status.HTTP_201_CREATED)

    #     except Exception as e:
    #         return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': f'Lỗi: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        try:
            sender_id = request.user.id
            receiver_id = request.query_params.get('receiver_id')

            sender = get_object_or_404(User, pk=sender_id)
            receiver = get_object_or_404(User, pk=receiver_id)

            if not sender or not receiver:
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Người dùng không tồn tại'}, status=status.HTTP_404_NOT_FOUND)

            messages = Message.objects.filter(
                (Q(sender=sender, receiver=receiver, sender_deleted=False) |
                Q(sender=receiver, receiver=sender, receiver_deleted=False))
            ).order_by('timestamp')

            messages_data = MessageSerializer(messages, many=True).data
            return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'messages': messages_data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': f'Lỗi: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            message_id = self.kwargs.get('message_id')
            message = get_object_or_404(Message, id=message_id)
            if not message:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Tin nhắn đã bị xóa trước đó'})

            message.delete()

            return Response({'status': status.HTTP_200_OK, 'message': 'Tin nhắn đã được thu hồi thành công'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': f'Lỗi: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#hiển thị tất cả tin nhắn của user với mn
# @api_view(['GET'])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def List_User_Messages(request):
#     try:
        
#         user_id = request.user.id
        
#         # Kiểm tra xem user_id có hợp lệ không
#         user = get_object_or_404(User, id=user_id)

#         # Lấy tất cả các id của người gửi hoặc người nhận tin nhắn, loại bỏ những người dùng đã xóa cuộc trò chuyện
#         sender_ids = Message.objects.filter(
#             (Q(sender=user, sender_deleted=False) | Q(receiver=user, receiver_deleted=False))
#         ).values_list('sender', flat=True).distinct()

#         receiver_ids = Message.objects.filter(
#             (Q(sender=user, sender_deleted=False) | Q(receiver=user, receiver_deleted=False))
#         ).values_list('receiver', flat=True).distinct()

#         # Kết hợp danh sách các id và loại bỏ id của chính user
#         user_ids = list(set(list(sender_ids) + list(receiver_ids)))

#         # Loại bỏ id của chính user
#         user_ids.remove(user.id)

#         # Lấy thông tin chi tiết về mỗi người dùng
#         user_details = []
#         for user_id in user_ids:
#             user = get_object_or_404(User, id=user_id)
#             user_data = {
#                 'id': user.id,
#                 'username': user.username,
#             }
#             user_details.append(user_data)

#         return Response({'status': status.HTTP_200_OK, 'message': 'Success','user_details': user_details})

#     except User.DoesNotExist:
#         return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Người dùng không tồn tại'})
#     except Exception as e:
#         return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Lỗi: {}'.format(str(e))})


#xóa cuộc hội thoại
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_conversation(request):
    try:
        user_id = request.user.id
        other_user_id = request.query_params.get('other_user_id') 

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

class Send_Message_ListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        logged_in_user = self.request.user

        # Lấy tất cả các id của người gửi hoặc người nhận tin nhắn
        sender_ids = Message.objects.filter(Q(sender=logged_in_user) & Q(sender_deleted=False)).values_list('receiver', flat=True).distinct() #lây ra những người nhận
        receiver_ids = Message.objects.filter(Q(receiver=logged_in_user) & Q(receiver_deleted=False)).values_list('sender', flat=True).distinct() #lây ra những người gửi

        # Kết hợp danh sách các id và loại bỏ id của chính user
        user_ids = list(set(list(sender_ids) + list(receiver_ids)))
        # Loại bỏ id của chính user
        user_ids.remove(logged_in_user.id)
        # Lấy thông tin chi tiết về mỗi người dùng
        user_details = []
        for user_id in user_ids:
            user = get_object_or_404(User, id=user_id)
            user_data = {
                'id': user.id,
                'username': user.username,
            }
            user_details.append(user_data)

        return user_details

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = User_Serializer(queryset, many=True)  # Sử dụng serializer cho User
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)  # Pass the request data to the serializer
        if serializer.is_valid():
            serializer.save()
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

# class Send_Message_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MessageSerializer
#     queryset = Message.objects.all()

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
        serializer = FollowListSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = FollowSerializer(data=request.data)  # Pass the request data to the serializer
        if serializer.is_valid():
            user_watching = request.data.get('watching')
            followers = request.data.get('followers')

            userr = User.objects.get(pk=user_watching)
            follower = User.objects.get(pk=followers)

            content = f"{follower.username} đã theo dõi bạn."
            Notification.objects.create(user=userr, user_send=follower, content=content)
            # Gửi thông báo qua email
            subject = 'Bạn có một thông báo mới'
            message = content
            from_email = 'quanghuyqb2001@gmial.com'  # Điền địa chỉ email của bạn
            recipient_list = [userr.email]

            send_mail(subject, message, from_email, recipient_list)

            serializer.save()
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
class Follow_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FollowListSerializer
    queryset = Follow.objects.all()
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


class ReviewView_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        try:
            # Lấy thông tin người dùng từ yêu cầu
            user_id = request.user.id
            user = get_object_or_404(User, pk=user_id)

            # Kiểm tra xem người dùng có tồn tại không
            if not user:
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Người dùng không tồn tại'}, status=status.HTTP_404_NOT_FOUND)
            reviews = Review.objects.filter(user_seller=user).order_by('timestamp')

            # Thực hiện xử lý trước khi trả về danh sách đánh giá
            processed_reviews_data = self.process_reviews(reviews)

            # Sử dụng serializer để chuyển đổi dữ liệu thành định dạng JSON
            serializer = self.get_serializer(processed_reviews_data, many=True)

            # Xây dựng dữ liệu response với thêm thông tin
            data = {'status': status.HTTP_200_OK, 'message': 'Success', 'reviews': serializer.data}

            # Trả về response
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': f'Lỗi: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def process_reviews(self, reviews):
        processed_reviews_data = []

        for review in reviews:
            processed_review = {
                'id': review.id,
                'comment': review.comment,
                'rating': review.rating,  # Thêm trường 'rating' vào đây
                'timestamp': review.timestamp,
                'user': review.user,
                'user_seller': review.user_seller,
                # Thêm hoặc thay đổi thông tin khác tùy thuộc vào yêu cầu của bạn
            }
            processed_reviews_data.append(processed_review)

        return processed_reviews_data
    def create(self, request, *args, **kwargs):
        # Kiểm tra xem rating có nằm trong khoảng từ 1 đến 5 không
        rating = request.data.get('rating')
        if not (1 <= rating <= 5):
            data = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Invalid rating. Rating must be between 1 and 5.'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
        user = request.data.get('user')
        user_seller = request.data.get('user_seller')
        queryset = Review.objects.filter(user=user,user_seller=user_seller)
        if queryset:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Can only be evaluated once', 'data': {}}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
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


class Notification_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return[]
        
    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        reviews = Notification.objects.filter(user=user).order_by('timestamp')
        notification_admin = Notification.objects.filter(notification_admin=True).order_by('timestamp')
        # Thực hiện xử lý trước khi trả về danh sách đánh giá
        if reviews is not None and notification_admin is not None:
            data_list = list(reviews) + list(notification_admin)
        else:
            # Xử lý khi một trong hai queryset là None
            data_list = []
        sorted_data_list = sorted(data_list, key=attrgetter('timestamp'), reverse=True)
        messages_data = NotificationSerializer(sorted_data_list, many=True).data
        return Response({'status': status.HTTP_200_OK, 'message': 'Success', 'messages': messages_data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid():
            serializer.save(notification_admin=True)
            data = {'status': status.HTTP_201_CREATED, 'message': 'Registered successfully', 'data': serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'status': status.HTTP_400_BAD_REQUEST,'message':'Registration failed', 'error': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class Notification_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
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

            