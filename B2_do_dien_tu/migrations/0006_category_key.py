# Generated by Django 5.0 on 2024-01-22 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B2_do_dien_tu', '0005_remove_category_parentcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='key',
            field=models.CharField(choices=[('DIENTHOAI', 'DIENTHOAI'), ('LAPTOP', 'LAPTOP'), ('MAYTINHBANG', 'MAYTINHBANG'), ('MAYTINHDEBAN', 'MAYTINHDEBAN'), ('CHUNG', 'CHUNG')], default=1, max_length=20, verbose_name='Key'),
            preserve_default=False,
        ),
    ]