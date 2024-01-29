from rest_framework import serializers,validators
from .models import *
from chotot.serializers import *


	
class NotificationSerializer(serializers.ModelSerializer):
    user = User_Serializer(read_only=True)
    user_send = User_Serializer(read_only=True)

    class Meta:
	    model=Notification
	    fields=('id','user', 'user_send', 'content', 'timestamp')