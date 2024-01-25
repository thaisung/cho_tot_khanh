from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from chotot.serializers import *

class Posted_news_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Posted_news
		fields='__all__'
					
class Poster_information_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Poster_information
		fields='__all__'

class Items_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Items_image
		fields='__all__'

class Items_Serializer(serializers.ModelSerializer):
	User = User_Serializer(read_only=True)
	images_A5 = Items_image_Serializer(many=True, read_only=True,source='Items_image_Items_A5')
	images_A5_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
	Posted_news = Posted_news_Serializer(read_only=True)
	Poster_information = Poster_information_Serializer(read_only=True)
	class Meta:
		model=Items
		fields='__all__'
		
