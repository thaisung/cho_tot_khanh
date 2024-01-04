# Generated by Django 5.0.1 on 2024-01-04 17:16

import A1_viec_lam.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Ngành nghề')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '1 - Ngành nghề',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Giới tính')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '5 - Kinh nghiệm',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Map', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vị trí bản đồ')),
                ('Title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tiêu đề')),
                ('Number_of_recruitment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Số lượng tuyển dụng')),
                ('Wage', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lương')),
                ('Detailed_description', models.TextField(blank=True, null=True, verbose_name='Mô tả chi tiết')),
                ('Minimum_age', models.CharField(blank=True, max_length=100, null=True, verbose_name='Độ tuổi tối thiểu')),
                ('Maximum_age', models.CharField(blank=True, max_length=100, null=True, verbose_name='Độ tuổi tối đa')),
                ('Video', models.FileField(blank=True, null=True, upload_to='A1/Job_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']), A1_viec_lam.models.validate_file_size])),
                ('Contact_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Số điện thoại liên hệ')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '6 - Việc làm',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Job_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='A1/Job_image')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '7 - Ảnh Sản phẩm mua bán Bất động sản',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pay_forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Hình thức trả lương')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '3 - Hình thức trả lương',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Giới tính')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '4 - Giới tính',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Type_of_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Loại công việc')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '2 - Loại công việc',
                'ordering': ['id'],
            },
        ),
    ]
