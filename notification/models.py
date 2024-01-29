from django.db import models
from chotot.models import User

class Notification(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông báo"
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name= 'user_notification', null=True)
    user_send = models.ForeignKey(User, on_delete=models.CASCADE,related_name= 'user_send_notification')
    content = models.TextField()
    notification_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    