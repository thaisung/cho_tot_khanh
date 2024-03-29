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
class Usage_status(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "1 - Tình trạng sử dụng"
    Name = models.CharField('Tên Tình trạng sử dụng',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
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
    
class Guarantee(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "3 - Bảo hành"
    Name = models.CharField('Tên Bảo hành',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
    
class Items(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Sản phẩm bán"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Items_User_A4')
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Items_Location_A4',verbose_name='Khu vực')
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Items_Address_A4',verbose_name='Địa chỉ')
    Usage_status = models.ForeignKey(Usage_status, on_delete=models.CASCADE, related_name='Items_Usage_status_A4',verbose_name='Tình trạng sử dụng')
    Guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE, related_name='Items_Guarantee_A3',verbose_name='Bảo hành')
    Free_giveaway = models.CharField('Tặng miễn phí',max_length=100, null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Seller_information = models.ForeignKey(Seller_information, on_delete=models.CASCADE, related_name='Items_Seller_information_A4',verbose_name='Thông tin người bán')
    Video = models.FileField(upload_to='A4/Items_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
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
    Items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='Items_images_Items_A4')
    Image = models.ImageField(upload_to='A4/Items_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Items.Title}"