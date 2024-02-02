# Generated by Django 5.0 on 2024-01-30 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A3_tu_lanh_may_lanh_may_giat', '0007_alter_items_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Volume',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Items_Volume_A3', to='A3_tu_lanh_may_lanh_may_giat.volume', verbose_name='Thể tích'),
        ),
    ]