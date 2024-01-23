from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from chotot.models import User
from chotot.models import Location,Address

def validate_file_size(value):
    max_size = 50 * 1024 * 1024  # 50 megabytes
    if value.size > max_size:
        raise ValidationError("File size must be no more than 50 megabytes.")

# Create your models here.
class Category(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "1 - Danh mục"
    Name = models.CharField('Tên Danh mục',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    key_category = {
        "MOTEL-ROOM-DORMITORY": "MOTEL-ROOM-DORMITORY",
        "WHOLE-HOUSE": "WHOLE-HOUSE",
        "BUSINESS-PREMISES": "BUSINESS-PREMISES",
    }
    keyForm =models.CharField('Key', choices=key_category.items(), max_length=50)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
	  
# class Location(models.Model):
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = "2 - Khu vực"
#     Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
#     Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
#     Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
#     Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
#     def __str__(self):	
#         return str(self.Name)
    
# class Address(models.Model):
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = "3 - Địa chỉ"
#     Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Address_Location_A2',verbose_name='Địa chỉ')
#     Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
#     Name_en = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
#     Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
#     Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
#     Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
#     def __str__(self):	
#         return str(self.Name)
    
class Interior_condition(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Tình trạng nội thất"
    Name = models.CharField('Tên Thể loại',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
	    
class Seller_information(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "5 - Dự án Bất động sản nổi bật"
    Name = models.CharField('Tên Danh mục',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Products(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "6 - Sản phẩm mua bán Bất động sản"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Products_User_A2')
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Products_Category_A2',verbose_name='Danh mục')
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Products_Location_A2',verbose_name='Khu vực')
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Products_Address_A2',verbose_name='Địa chỉ')
    Acreage = models.CharField('Diện tích',max_length=100, null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Deposit_amount = models.CharField('Số tiền cọc',max_length=100, null=True, blank=True)
    Interior_condition = models.ForeignKey(Interior_condition, on_delete=models.CASCADE, related_name='Products_Interior_condition_A2',verbose_name='Tình trạng nội thất')
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Seller_information = models.ForeignKey(Seller_information, on_delete=models.CASCADE, related_name='Products_Seller_information_A2',verbose_name='Thông tin người bán')
    Number_of_bedrooms = models.CharField('Số phòng ngủ',max_length=100, null=True, blank=True)
    Number_of_bathrooms = models.CharField('Số phòng vệ sinh',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Video = models.FileField(upload_to='A2/Products_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
    Contact_phone_number = models.CharField('Số điện thoại liên hệ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Title)
    
class Products_image(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "7 - Ảnh Sản phẩm mua bán Bất động sản"
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='Products_image_Products_A2')
    Image = models.ImageField(upload_to='A2/Products_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Product.Title}"
    
