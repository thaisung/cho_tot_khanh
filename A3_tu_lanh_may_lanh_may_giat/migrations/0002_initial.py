# Generated by Django 5.0.1 on 2024-01-04 17:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('A3_tu_lanh_may_lanh_may_giat', '0001_initial'),
        ('chotot', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='Address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Address_A3', to='chotot.address', verbose_name='Địa chỉ'),
        ),
        migrations.AddField(
            model_name='items',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Category_A3', to='A3_tu_lanh_may_lanh_may_giat.category', verbose_name='Danh mục'),
        ),
        migrations.AddField(
            model_name='items',
            name='Guarantee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Guarantee_A3', to='A3_tu_lanh_may_lanh_may_giat.guarantee', verbose_name='Bảo hành'),
        ),
        migrations.AddField(
            model_name='items',
            name='Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Location_A3', to='chotot.location', verbose_name='Khu vực'),
        ),
        migrations.AddField(
            model_name='items',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_User_A3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='items_image',
            name='Items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_image_Items_A3', to='A3_tu_lanh_may_lanh_may_giat.items'),
        ),
        migrations.AddField(
            model_name='items',
            name='Seller_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Seller_information_A3', to='A3_tu_lanh_may_lanh_may_giat.seller_information', verbose_name='Thông tin người bán'),
        ),
        migrations.AddField(
            model_name='items',
            name='Usage_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Usage_status_A3', to='A3_tu_lanh_may_lanh_may_giat.usage_status', verbose_name='Tình trạng sử dụng'),
        ),
        migrations.AddField(
            model_name='items',
            name='Volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Volume_A3', to='A3_tu_lanh_may_lanh_may_giat.volume', verbose_name='Thể tích'),
        ),
        migrations.AddField(
            model_name='items',
            name='Washing_volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Washing_volume_A3', to='A3_tu_lanh_may_lanh_may_giat.washing_volume', verbose_name='Khối lượng giặt'),
        ),
        migrations.AddField(
            model_name='items',
            name='Wattage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items_Wattage_A3', to='A3_tu_lanh_may_lanh_may_giat.wattage', verbose_name='Công suất'),
        ),
    ]
