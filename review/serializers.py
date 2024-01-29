from rest_framework import serializers,validators
from .models import *
from chotot.serializers import *


class ReviewSerializer(serializers.ModelSerializer):
	user = User_Serializer(read_only=True)
	user_seller = User_Serializer(read_only=True)
	class Meta:
		model=Review
		fields='__all__'
	
