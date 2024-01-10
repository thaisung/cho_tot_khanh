from django.db import models
from chotot.models import User

class Message(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý Message"
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    sender_deleted = models.BooleanField(default=False)
    receiver_deleted = models.BooleanField(default=False)

class Follow(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Theo dõi"

    followers = models.ManyToManyField(User, related_name='user_followed', null=True, blank=True)
    watching = models.ManyToManyField(User, related_name='user_follow', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Review(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Đánh giá"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_review')
    user_seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_seller_review')
    rating = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

