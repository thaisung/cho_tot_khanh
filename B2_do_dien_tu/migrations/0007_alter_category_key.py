# Generated by Django 5.0 on 2024-01-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B2_do_dien_tu', '0006_category_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='key',
            field=models.CharField(choices=[('DIENTHOAI', 'DIENTHOAI'), ('LAPTOP', 'LAPTOP'), ('MAYTINHBANG', 'MAYTINHBANG'), ('MAYTINHDEBAN', 'MAYTINHDEBAN'), ('COMMON-ELECTRONICE-DEVICE', 'COMMON-ELECTRONICE-DEVICE')], max_length=50, verbose_name='Key'),
        ),
    ]
