# Generated by Django 4.2.6 on 2023-10-19 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0003_auto_20210209_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='adoption_date',
        ),
    ]
