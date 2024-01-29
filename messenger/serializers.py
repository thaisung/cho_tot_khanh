from rest_framework import serializers,validators
from .models import *
from chotot.serializers import *


class MessageSerializer(serializers.ModelSerializer):
    sender = User_Serializer(read_only=True)
    receiver = User_Serializer(read_only=True)
    
    class Meta:
        model = Message
        fields = ('id','sender', 'receiver', 'content','id_products','url_parent', 'timestamp')
    
