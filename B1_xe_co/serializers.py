from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from chotot.serializers import *

class B1CategorySerializer(serializers.ModelSerializer):
    # Sử dụng ParentCategory_Serializer cho trường ParentCategory
    ParentCategory = ParentCategory_Serializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class B1CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class B1YearOfManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year_of_manufacture
        fields = '__all__'

class B1GearboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gearbox
        fields = '__all__'

class B1FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'

class B1GuaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantee
        fields = '__all__'

class B1SeatNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat_number
        fields = '__all__'

class B1UsageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage_status
        fields = '__all__'

class B1SellerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_information
        fields = '__all__'

class B1CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacity
        fields = '__all__'

class B1Items_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Items_image
		fields='__all__'

class B1Items_Serializer(serializers.ModelSerializer):
    User = User_Serializer(read_only=True)
    images_A3 = B1Items_image_Serializer(many=True, read_only=True, source='Items_image_Items_B1')
    images_A3_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    Location = Location_Serializer(read_only=True)
    Address = Address_Serializer(read_only=True)
    Category = B1CategorySerializer(read_only=True)
    Usage_status = B1UsageStatusSerializer(read_only=True)
    Seller_information = B1SellerInformationSerializer(read_only=True)
    Guarantee = B1GuaranteeSerializer(read_only=True)
    Company = B1CompanySerializer(read_only=True)
    Year_of_manufacture = B1YearOfManufactureSerializer(read_only=True)
    Gearbox = B1GearboxSerializer(read_only=True)
    Fuel = B1FuelSerializer(read_only=True)
    Seat_number = B1SeatNumberSerializer(read_only=True)
    Capacity = B1CapacitySerializer(read_only=True)

    class Meta:
        model = ItemsB1
        fields = '__all__'
        extra_kwargs = {
            'Location': {'write_only': True},  # không xuất hiện đầu ra trong api
        }
