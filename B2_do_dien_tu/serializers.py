from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from chotot.serializers import *


class B2CategorySerializer(serializers.ModelSerializer):
    ParentCategory = ParentCategory_Serializer(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class B2UsageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage_status
        fields = '__all__'

class B2CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class B2ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class B2CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacity
        fields = '__all__'

class B2GuaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantee
        fields = '__all__'

class B2MicroprocessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microprocessor
        fields = '__all__'

class B2RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'

class B2HardDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hard_drive
        fields = '__all__'

class B2MonitorCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor_card
        fields = '__all__'

class B2ScreenSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen_size
        fields = '__all__'

class B2SellerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_information
        fields = '__all__'

class B2Items_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Items_image
		fields='__all__'
        
class B2Items_Serializer(serializers.ModelSerializer):
    User = User_Serializer(read_only=True)
    images_A3 = B2Items_image_Serializer(many=True, read_only=True, source='Items_image_Items_B2')
    images_A3_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    Location = Location_Serializer(read_only=True)
    Address = Address_Serializer(read_only=True)
    Category = B2CategorySerializer(read_only=True)
    Usage_status = B2UsageStatusSerializer(read_only=True)
    Seller_information = B2SellerInformationSerializer(read_only=True)
    Guarantee = B2GuaranteeSerializer(read_only=True)
    Company = B2CompanySerializer(read_only=True)
    Color = B2ColorSerializer(read_only=True)
    Capacity = B2CapacitySerializer(read_only=True)
    Microprocessor = B2MicroprocessorSerializer(read_only=True)
    Ram = B2RamSerializer(read_only=True)
    HardDrive = B2HardDriveSerializer(read_only=True)
    MonitorCard = B2MonitorCardSerializer(read_only=True)
    ScreenSize = B2ScreenSizeSerializer(read_only=True)
    
    
    class Meta:
        model = ItemsB2
        fields = '__all__'
        extra_kwargs = {
            'Location': {'write_only': True},  # không xuất hiện đầu ra trong api
        }