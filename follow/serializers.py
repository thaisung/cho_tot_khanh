from rest_framework import serializers,validators
from .models import *
from chotot.serializers import *


class FollowSerializer(serializers.ModelSerializer):
	followers = User_Serializer(read_only=True)
	watching = User_Serializer(read_only=True)
	class Meta:
		model=Follow
		fields='__all__'

		extra_kwargs = {
            'user': {'write_only': True},
            'user_seller': {'write_only': True},
        }
