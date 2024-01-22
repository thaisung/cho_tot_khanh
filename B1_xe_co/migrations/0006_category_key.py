# Generated by Django 5.0 on 2024-01-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B1_xe_co', '0005_remove_category_parentcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='key',
            field=models.CharField(choices=[('OTO', 'OTO'), ('XEMAY', 'XEMAY'), ('CHUNG', 'CHUNG')], default=1, max_length=10, verbose_name='Key'),
            preserve_default=False,
        ),
    ]