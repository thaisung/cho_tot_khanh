# Generated by Django 5.0 on 2024-01-20 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('B5_cua_hang_viet', '0004_category_parentcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='ParentCategory',
        ),
    ]
