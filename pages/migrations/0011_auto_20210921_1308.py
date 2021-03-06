# Generated by Django 3.2.4 on 2021-09-21 07:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_testimonail_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonail',
            name='testimonial_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='testimonial_image'),
        ),
        migrations.AlterField(
            model_name='work',
            name='photo_main',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='work'),
        ),
    ]
