# Generated by Django 3.2.3 on 2021-06-14 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_images_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image1',
        ),
    ]
