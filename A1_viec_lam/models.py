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
class Career(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "1 - Ngành nghề"
    Name = models.CharField('Tên Ngành nghề',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
	
class Type_of_work(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "2 - Loại công việc"
    Name = models.CharField('Tên Loại công việc',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Pay_forms(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "3 - Hình thức trả lương"
    Name = models.CharField('Tên Hình thức trả lương',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
# class Location(models.Model):
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = "4 - Khu vực"
#     Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
#     Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
#     Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
#     Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
#     def __str__(self):	
#         return str(self.Name)
    
# class Address(models.Model):
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = "5 - Địa chỉ"
#     Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Address_Location_A1',verbose_name='Địa chỉ')
#     Name = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
#     Name_en = models.CharField('Tên Khu vực',max_length=100, null=True, blank=True)
#     Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
#     Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
#     Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
#     def __str__(self):	
#         return str(self.Name)

class Sex(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "4 - Giới tính"
    Name = models.CharField('Tên Giới tính',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Experience(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "5 - Kinh nghiệm"
    Name = models.CharField('Tên Giới tính',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Name)
    
class Job(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "6 - Việc làm"
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Job_User_A1')
    Map = models.CharField('Vị trí bản đồ',max_length=100, null=True, blank=True)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Job_Location_A1',verbose_name='Khu vực')
    Address =  models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Job_Address_A1',verbose_name='Địa chỉ')
    Title = models.CharField('Tiêu đề',max_length=100, null=True, blank=True)
    Number_of_recruitment = models.CharField('Số lượng tuyển dụng',max_length=100, null=True, blank=True)
    Career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='Job_Career_A1',verbose_name='Nghành nghề')
    Type_of_work = models.ForeignKey(Type_of_work, on_delete=models.CASCADE, related_name='Job_Type_of_work_A1',verbose_name='Loại công việc')
    Pay_forms = models.ForeignKey(Pay_forms, on_delete=models.CASCADE, related_name='Job_Pay_forms_A1',verbose_name='Hình thức trả lương')
    Wage = models.CharField('Lương',max_length=100, null=True, blank=True)
    Detailed_description = models.TextField('Mô tả chi tiết',blank=True, null=True)
    Minimum_age = models.CharField('Độ tuổi tối thiểu',max_length=100, null=True, blank=True)
    Maximum_age = models.CharField('Độ tuổi tối đa',max_length=100, null=True, blank=True)
    Sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name='Job_Sex_A1',verbose_name='Giới tính')
    Experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='Job_Experience_A1',verbose_name='Kinh nghiệm')
    Video = models.FileField(upload_to='A1/Job_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),validate_file_size,],null=True, blank=True)
    Contact_phone_number = models.CharField('Số điện thoại liên hệ',max_length=100, null=True, blank=True)
    Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return str(self.Title)
    
class Job_image(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "7 - Ảnh Sản phẩm mua bán Bất động sản"
    Job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='Job_image_Job_A1')
    Image = models.ImageField(upload_to='A1/Job_image')
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    def __str__(self):	
        return f"Image for {self.Job.Title}"