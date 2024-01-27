from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from chotot.serializers import *

class Category_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields='__all__'
		ref_name = 'A2Category'
		
class Interior_condition_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Interior_condition
		fields='__all__'
				
class Seller_information_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Seller_information
		fields='__all__'
		ref_name = 'A2SellerInformation'

class Products_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Products_image
		fields='__all__'
	def get_image_url(self, instance):
		request = self.context.get('request', None)
		if request and instance.image:
			return request.build_absolute_uri(instance.image.url)
		return None

class Products_Serializer(serializers.ModelSerializer):
	User = User_Serializer(read_only=True)
	images_A2 = Products_image_Serializer(many=True, read_only=True,source='Products_image_Products_A2')
	images_A2_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
	Location = Location_Serializer(read_only=True)
	Address = Address_Serializer(read_only=True)
	Category = Category_Serializer(read_only=True)
	Interior_condition = Interior_condition_Serializer(read_only=True)
	Seller_information = Seller_information_Serializer(read_only=True)
	class Meta:
		model=Products
		fields='__all__'
		extra_kwargs = {
            'Location': {'write_only': True}, #ko xuất hiện đầu ra trong api
        }
		
		
