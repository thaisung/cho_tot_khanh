# Generated by Django 5.0 on 2024-01-20 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('B1_xe_co', '0005_remove_category_parentcategory'),
        ('B2_do_dien_tu', '0005_remove_category_parentcategory'),
        ('B3_dich_vu', '0005_remove_category_parentcategory'),
        ('B4_do_gia_dung_noi_that', '0005_remove_category_parentcategory'),
        ('B5_cua_hang_viet', '0005_remove_category_parentcategory'),
        ('chotot', '0005_rename_parent_category_parentcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParentCategory',
        ),
    ]
