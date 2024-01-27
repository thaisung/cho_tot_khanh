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
		ref_name = 'A3Category'
					
class Usage_status_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Usage_status
		fields='__all__'
		ref_name = 'A3UsageStatus'

class Seller_information_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Seller_information
		fields='__all__'

class Guarantee_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Guarantee
		fields='__all__'
		ref_name = 'A3Guarantee'

class Volume_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Volume
		fields='__all__'

class Wattage_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Wattage
		fields='__all__'

class Washing_volume_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Washing_volume
		fields='__all__'
					
class Items_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Items_image
		fields='__all__'
		ref_name = 'A3ItemsImage'
	def get_image_url(self, instance):
		request = self.context.get('request', None)
		if request and instance.image:
			return request.build_absolute_uri(instance.image.url)
		return None

class Items_Serializer(serializers.ModelSerializer):
	User = User_Serializer(read_only=True)
	images_A3 = Items_image_Serializer(many=True, read_only=True,source='Items_image_Items_A3')
	images_A3_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
	Location = Location_Serializer(read_only=True)
	Address = Address_Serializer(read_only=True)
	Category = Category_Serializer(read_only=True)
	Usage_status = Usage_status_Serializer(read_only=True)
	Seller_information = Seller_information_Serializer(read_only=True)
	Guarantee = Guarantee_Serializer(read_only=True)
	Volume = Volume_Serializer(read_only=True)
	Wattage = Wattage_Serializer(read_only=True)
	Washing_volume = Washing_volume_Serializer(read_only=True)
	class Meta:
		model=Items
		fields='__all__'
		extra_kwargs = {
            'Location': {'write_only': True}, #ko xuất hiện đầu ra trong api
        }
		ref_name = 'A3Items'