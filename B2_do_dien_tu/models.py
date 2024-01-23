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
    # ParentCategory = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, related_name='Parent_Category_B2',verbose_name='Danh mục cha')
    key_category = {
        "PHONE": "PHONE",
        "LAPTOP": "LAPTOP",
        "TABLET": "TABLET",
        "DESKTOP": "DESKTOP",
        "COMMON-ELECTRONICE-DEVICE": "COMMON-ELECTRONICE-DEVICE",
    }
    keyForm =models.CharField('Key', choices=key_category.items(), max_length=50)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Usage_status(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "2 - Tình trạng sử dụng"
    Name = models.CharField('Tên Tình trạng sử dụng',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Company(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "3 - Hãng"
    Name = models.CharField('Tên hãng xe',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Color(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Màu sắc"
    Name = models.CharField('Tên hãng xe',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Capacity(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "5 - Dung lượng"
    Name = models.CharField('Tên Tình trạng sử dụng',max_length=100, null=True, blank=True)
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

class Microprocessor(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "7 - Bộ vi xử lý"
    Name = models.CharField('Tên hãng xe',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Ram(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "8 - Ram"
    Name = models.CharField('Tên hãng xe',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Hard_drive(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "9 - Ổ cứng"
    Name = models.CharField('Tên Tình trạng sử dụng',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Monitor_card(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "10 - Car màn hình"
    Name = models.CharField('Tên bảo hành',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Screen_size(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "11 - kích cỡ màn hình"
    Name = models.CharField('Tên hãng xe',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)

class Seller_information(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "12 - Thông tin người bán"
    Name = models.CharField('Tên Thông tin người bán',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
        
class ItemsB2(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "13 - Sản phẩm bán xe cộ"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Items_User_B2')
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Items_Location_B2',verbose_name='Khu vực')
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Items_Address_B2',verbose_name='Địa chỉ')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Items_Category_B2',verbose_name='Danh mục')
    Usage_status = models.ForeignKey(Usage_status, on_delete=models.CASCADE, related_name='Items_Usage_status_B2',verbose_name='Tình trạng sử dụng')
    Seller_information = models.ForeignKey(Seller_information, on_delete=models.CASCADE, related_name='Items_Seller_information_B2',verbose_name='Thông tin người bán')
    Guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, related_name='Items_Guarantee_B2',verbose_name='Bảo hành')
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='Items_Company_B2',verbose_name='Hãng',null=True)
    Color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='Items_Color_B2',verbose_name='Màu sắc',null=True)
    Capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE, related_name='Items_Capacity_B2',verbose_name='Dung lượng',null=True)
    Microprocessor = models.ForeignKey(Microprocessor, on_delete=models.CASCADE, related_name='Items_Microprocessor_B2',verbose_name='Bộ vi xử lý', null=True)
    Ram = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='Items_Ram_B2',verbose_name='Ram', null=True)
    Hard_drive = models.ForeignKey(Hard_drive, on_delete=models.CASCADE, related_name='Items_Hard_drive_B2',verbose_name='Ổ cứng',null=True)
    Monitor_card = models.ForeignKey(Monitor_card, on_delete=models.CASCADE, related_name='Items_Monitor_card_B2',verbose_name='Car màn hình',null=True)
    Screen_size = models.ForeignKey(Screen_size, on_delete=models.CASCADE, related_name='Items_Screen_size_B2',verbose_name='Kích cớ màn hình', null=True)
    Free_giveaway = models.CharField('Tặng miễn phí',max_length=100, null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Video = models.FileField(upload_to='B2/Items_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
    Contact_phone_number = models.CharField('Số điện thoại liên hệ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def __str__(self):	
        return str(self.Title)

class Items_image(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "12 - Ảnh Sản phẩm đồ điện tử"
    Items = models.ForeignKey(ItemsB2, on_delete=models.CASCADE, related_name='Items_image_Items_B2')
    Image = models.ImageField(upload_to='B2/Items_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Items.Title}"