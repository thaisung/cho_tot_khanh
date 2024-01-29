from django.db import models
from chotot.models import User
# Create your models here.
class Follow(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Theo dõi"

    followers = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_followed', null=True, blank=True)
    watching = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_follow', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
