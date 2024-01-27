from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests
from chotot.serializers import *

class Career_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Career
		fields='__all__'
		
class Type_of_work_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Type_of_work
		fields='__all__'
		
class Pay_forms_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Pay_forms
		fields='__all__'

class Sex_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Sex
		fields='__all__'

class Experience_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Experience
		fields='__all__'
		
class Job_image_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Job_image
		fields='__all__'
	def get_image_url(self, instance):
		request = self.context.get('request', None)
		if request and instance.image:
			return request.build_absolute_uri(instance.image.url)
		return None

class Job_Serializer(serializers.ModelSerializer):
	User = User_Serializer(read_only=True)
	images_A1 = Job_image_Serializer(many=True, read_only=True,source='Job_image_Job_A1')
	images_A1_data = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
	Location = Location_Serializer(read_only=True)
	Address = Address_Serializer(read_only=True)
	Career = Career_Serializer(read_only=True)
	Type_of_work = Type_of_work_Serializer(read_only=True)
	Pay_forms = Pay_forms_Serializer(read_only=True)
	Sex = Sex_Serializer(read_only=True)
	Experience = Experience_Serializer(read_only=True)
	class Meta:
		model=Job
		fields='__all__'
		extra_kwargs = {
            'Location': {'write_only': True}, #ko xuất hiện đầu ra trong api
        }
