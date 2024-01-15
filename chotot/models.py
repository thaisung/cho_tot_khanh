from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý tài khoản"
    AbstractUser._meta.get_field('email').blank = True
    AbstractUser._meta.get_field('email').null = True
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('username').null = False
    AbstractUser._meta.get_field('password').blank = False
    AbstractUser._meta.get_field('password').null = False
    avatar = models.ImageField(upload_to='chotot/User_image',null=True,blank=True)
    registration_type = models.CharField('Loại dăng ký',max_length=100, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    last_logout = models.DateTimeField(null=True, blank=True)
     
# class Category(models.Model):
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = "1 - Danh mục"
#     Name = models.CharField('Tên Danh mục',max_length=100, null=True, blank=True)
#     Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
#     Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
#     Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
#     def __str__(self):	
#         return str(self.Name)

class Location(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "1 - Khu vực"
    Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Address(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "2 - Địa chỉ"
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Address_Location',verbose_name='Địa chỉ')
    Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
    Name_en = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class ParentCategory(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "3 - Danh mục cha"
    Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to='chotot/Parent_Category_image')
    Icon  = models.FileField(upload_to='chotot/icon')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    