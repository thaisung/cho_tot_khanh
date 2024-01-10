from rest_framework import serializers,validators
from .models import *
from chotot.serializers import *


class MessageSerializer(serializers.ModelSerializer):
    sender = User_Serializer(read_only=True)
    receiver = User_Serializer(read_only=True)
    class Meta:
        model = Message
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
	# followers = User_Serializer(read_only=True)
	# watching = User_Serializer(read_only=True)
	class Meta:
		model=Follow
		fields='__all__'

		extra_kwargs = {
            'user': {'write_only': True},
            'user_seller': {'write_only': True},
        }

class FollowListSerializer(serializers.ModelSerializer):
    followers = User_Serializer(read_only=True,many=True)
    watching = User_Serializer(read_only=True,many=True)
    class Meta:
        model=Follow
        fields='__all__'


class ReviewSerializer(serializers.ModelSerializer):
	user = User_Serializer(read_only=True)
	user_seller = User_Serializer(read_only=True)
	class Meta:
		model=Review
		fields='__all__'
	