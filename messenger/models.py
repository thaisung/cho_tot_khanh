from django.db import models
from chotot.models import User

class Message(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý Message"
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    id_products = models.CharField(max_length = 50)
    url_parent =  models.CharField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    sender_deleted = models.BooleanField(default=False)
    receiver_deleted = models.BooleanField(default=False)