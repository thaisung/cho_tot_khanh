# Generated by Django 5.0.1 on 2024-01-04 15:41

import A3_tu_lanh_may_lanh_may_giat.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Danh mục')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '1 - Danh mục',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Bảo hành')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '4 - Bảo hành',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Map', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vị trí bản đồ')),
                ('Free_giveaway', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tặng miễn phí')),
                ('Price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Giá')),
                ('Title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tiêu đề')),
                ('Detailed_description', models.TextField(blank=True, null=True, verbose_name='Mô tả chi tiết')),
                ('Video', models.FileField(blank=True, null=True, upload_to='A3/Items_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']), A3_tu_lanh_may_lanh_may_giat.models.validate_file_size])),
                ('Contact_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Số điện thoại liên hệ')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '8 - Sản phẩm bán',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Items_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='A3/Items_image')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '9 - Ảnh Sản phẩm Thời trang đồ dùng cá nhân',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Seller_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Thông tin người bán')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '3 - Thông tin người bán',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Usage_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Tình trạng sử dụng')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '2 - Tình trạng sử dụng',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Thể tích')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '5 - Thể tích',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Washing_volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Công suất')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '7 - Khối lượng giặt',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Wattage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên Công suất')),
                ('Url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đường dẫn')),
                ('Creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('Update_time', models.DateTimeField(auto_now=True, verbose_name='Thời gian cập nhật')),
            ],
            options={
                'verbose_name_plural': '6 - Công suất',
                'ordering': ['id'],
            },
        ),
    ]