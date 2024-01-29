from django.db import models
from chotot.models import User

# Create your models here.
class Review(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Đánh giá"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_review')
    user_seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_seller_review')
    rating = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)