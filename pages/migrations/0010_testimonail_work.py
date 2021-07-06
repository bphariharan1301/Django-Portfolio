# Generated by Django 3.2.4 on 2021-07-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20210701_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_name', models.CharField(max_length=30)),
                ('testimonial_location', models.CharField(max_length=50)),
                ('testimonial_image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('category', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
