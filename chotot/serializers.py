from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests

# class Category_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Category
# 		fields='__all__'

class User_Serializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','registration_type','avatar','username','password', 'email','first_name','last_name','is_staff','is_superuser','last_updated','last_login','last_logout','date_joined']
		read_only_fields = ['date_joined'] #chỉ đọc ko dc ghi
		extra_kwargs = {
            'password': {'write_only': True}, #ko xuất hiện đầu ra trong api
        }

class Address_Serializer(serializers.ModelSerializer):
	# Location = Location_Serializer(read_only=True)
	class Meta:
		model=Address
		fields='__all__'
		depth = 1			
class Location_Serializer(serializers.ModelSerializer):
	Address_Location = Address_Serializer(many=True, read_only=True)
	class Meta:
		model=Location
		fields='__all__'
		depth = 1
# class Address_Serializer(serializers.ModelSerializer):
	# Location = Location_Serializer(read_only=True)
# 	class Meta:
# 		model=Address
# 		fields='__all__'
# 		depth = 1
		
# class ParentCategory_Serializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=ParentCategory
# 		fields='__all__'