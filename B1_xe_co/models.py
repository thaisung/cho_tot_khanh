from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from chotot.models import User
from chotot.models import Location,Address
from chotot.serializers import *

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
    # ParentCategory = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, related_name='Parent_Category_B1',verbose_name='Danh mục cha')
    key_category = {
        "CAR": "CAR",
        "MOTORBIKE": "MOTORBIKE",
        "COMMON-VEHICLE": "COMMON-VEHICLE",
    }
    key = models.CharField('Key', choices=key_category.items(), max_length=50)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Company(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "2 - Hãng xe"
    Name = models.CharField('Tên hãng xe',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Year_of_manufacture(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "3 - Năm sản xuất"
    Name = models.CharField('Tên sản xuất',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Gearbox(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Hộp số "
    Name = models.CharField('Tên hộp số',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Fuel(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "5 - Nhiên liệu"
    Name = models.CharField('Tên hộp số',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Guarantee(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "6 - Bảo hành"
    Name = models.CharField('Tên bảo hành',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Seat_number(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "7 - Số chổ"
    Name = models.CharField('Tên số chổ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Usage_status(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "8 - Tình trạng sử dụng"
    Name = models.CharField('Tên Tình trạng sử dụng',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Seller_information(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "9 - Thông tin người bán"
    Name = models.CharField('Tên Thông tin người bán',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Capacity(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "10 - Dung tích"
    Name = models.CharField('Tên dung tích',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)


class ItemsB1(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "11 - Sản phẩm bán xe cộ"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Items_User_B1')
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Items_Location_B1',verbose_name='Khu vực')
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Items_Address_B1',verbose_name='Địa chỉ')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Items_Category_B1',verbose_name='Danh mục')
    Usage_status = models.ForeignKey(Usage_status, on_delete=models.CASCADE, related_name='Items_Usage_status_B1',verbose_name='Tình trạng sử dụng')
    Seller_information = models.ForeignKey(Seller_information, on_delete=models.CASCADE, related_name='Items_Seller_information_B1',verbose_name='Thông tin người bán')
    Guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, related_name='Items_Guarantee_B1',verbose_name='Bảo hành')
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='Items_Company_B1',verbose_name='Hãng xe',null=True)
    Year_of_manufacture = models.ForeignKey(Year_of_manufacture, on_delete=models.CASCADE, related_name='Items_Year_of_manufacture_B1',verbose_name='Năm sản xuất',null=True)
    Gearbox = models.ForeignKey(Gearbox, on_delete=models.CASCADE, related_name='Items_Gearbox_B1',verbose_name='Hộp số',null=True)
    Fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name='Items_Fuel_B1',verbose_name='Nhiên liệu', null=True)
    Seat_number = models.ForeignKey(Seat_number, on_delete=models.CASCADE, related_name='Items_Seat_number_B1',verbose_name='Số chổ', null=True)
    Capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE, related_name='Items_Capacity_B1',verbose_name='Dung tích',null=True)
    Free_giveaway = models.CharField('Tặng miễn phí',max_length=100, null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Video = models.FileField(upload_to='B1/Items_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
    Contact_phone_number = models.CharField('Số điện thoại liên hệ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def __str__(self):	
        return str(self.Title)

class Items_image(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "12 - Ảnh Sản phẩm xe cộ"
    Items = models.ForeignKey(ItemsB1, on_delete=models.CASCADE, related_name='Items_image_Items_B1')
    Image = models.ImageField(upload_to='B1/Items_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Items.Title}"