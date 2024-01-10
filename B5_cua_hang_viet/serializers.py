from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from chotot.serializers import *


class B5CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class B5SellerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_information
        fields = '__all__'

class B5Items_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Items_image
		fields='__all__'
        
class B5Items_Serializer(serializers.ModelSerializer):
    User = User_Serializer(read_only=True)
    images_A3 = B5Items_image_Serializer(many=True, read_only=True, source='Items_image_Items_B5')
    images_A3_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    Location = Location_Serializer(read_only=True)
    Address = Address_Serializer(read_only=True)
    Category = B5CategorySerializer(read_only=True)
    Seller_information = B5SellerInformationSerializer(read_only=True)
   

    class Meta:
        model = Items
        fields = '__all__'
        extra_kwargs = {
            'Location': {'write_only': True},  # không xuất hiện đầu ra trong api
        }