from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from chotot.models import User
from chotot.models import Location,Address
# from chotot.serializers import *

def validate_file_size(value):
    max_size = 50 * 1024 * 1024  # 50 megabytes
    if value.size > max_size:
        raise ValidationError("File size must be no more than 50 megabytes.")

class Category(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "1 - Danh mục"
    Name = models.CharField('Tên Danh mục',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    # ParentCategory = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, related_name='Parent_Category_B5',verbose_name='Danh mục cha')
    key_category = {
        "COMMON-VIETSHOP": "COMMON-VIETSHOP" 
    }
    key = models.CharField('Key', choices=key_category.items(), max_length=50)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Seller_information(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "2 - Thông tin người bán"
    Name = models.CharField('Tên Thông tin người bán',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
        
class ItemsB5(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "3 - Sản phẩm shop việt"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Items_User_B5')
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Items_Location_B5',verbose_name='Khu vực')
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Items_Address_B5',verbose_name='Địa chỉ')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Items_Category_B5',verbose_name='Danh mục')
    Seller_information = models.ForeignKey(Seller_information, on_delete=models.CASCADE, related_name='Items_Seller_information_B5',verbose_name='Thông tin người bán')
    Free_giveaway = models.CharField('Tặng miễn phí',max_length=100, null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Video = models.FileField(upload_to='B5/Items_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
    Contact_phone_number = models.CharField('Số điện thoại liên hệ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def __str__(self):	
        return str(self.Title)

class Items_image(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Ảnh Sản phẩm"
    Items = models.ForeignKey(ItemsB5, on_delete=models.CASCADE, related_name='Items_image_Items_B5')
    Image = models.ImageField(upload_to='B5/Items_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Items.Title}"