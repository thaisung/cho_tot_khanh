# Generated by Django 5.0 on 2024-01-24 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A2_nha_tot', '0003_category_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='key',
            new_name='keyForm',
        ),
    ]