# Generated by Django 5.0 on 2024-01-25 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A5_taxi', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='Location',
        ),
    ]
