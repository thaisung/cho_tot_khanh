# Generated by Django 5.0 on 2024-01-29 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='id_products',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='url_parent',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]