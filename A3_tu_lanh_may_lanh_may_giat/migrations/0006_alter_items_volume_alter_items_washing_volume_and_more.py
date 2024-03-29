# Generated by Django 5.0 on 2024-01-30 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A3_tu_lanh_may_lanh_may_giat', '0005_alter_items_volume_alter_items_washing_volume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Volume',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Items_Volume_A3', to='A3_tu_lanh_may_lanh_may_giat.volume', verbose_name='Thể tích'),
        ),
        migrations.AlterField(
            model_name='items',
            name='Washing_volume',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Items_Washing_volume_A3', to='A3_tu_lanh_may_lanh_may_giat.washing_volume', verbose_name='Khối lượng giặt'),
        ),
        migrations.AlterField(
            model_name='items',
            name='Wattage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Items_Wattage_A3', to='A3_tu_lanh_may_lanh_may_giat.wattage', verbose_name='Công suất'),
        ),
    ]
