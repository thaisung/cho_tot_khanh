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
class Posted_news(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "1 - Tin đăng"
    Name = models.CharField('Tên Tin đăng',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Poster_information(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "2 - Thông tin người đăng"
    Name = models.CharField('Tên Thông tin người đăng',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Items(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Sản phẩm bán"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Items_User_A5',null=True, blank=True)
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Items_Address_A5',verbose_name='Địa chỉ',null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Posted_news = models.ForeignKey(Posted_news, on_delete=models.CASCADE, related_name='Items_Posted_news_A5',verbose_name='Tin dăng',null=True, blank=True)
    Place_of_origin = models.CharField('Nơi xuất phát',max_length=100, null=True, blank=True)
    Destination = models.CharField('Nơi đến',max_length=100, null=True, blank=True)
    Time_to_start_moving = models.CharField('Ngày đi',max_length=100, null=True, blank=True)
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Poster_information = models.ForeignKey(Poster_information, on_delete=models.CASCADE, related_name='Items_Poster_information_A5',verbose_name='Thông tin người đăng',null=True, blank=True)
    Video = models.FileField(upload_to='A5/Items_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
    Contact_phone_number = models.CharField('Số điện thoại liên hệ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Title)
    
class Items_image(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "9 - Ảnh Sản phẩm Thời trang đồ dùng cá nhân"
    Items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='Items_image_Items_A5')
    Image = models.ImageField(upload_to='A5/Items_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Items.Title}"