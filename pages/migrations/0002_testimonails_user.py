# Generated by Django 3.2.4 on 2021-06-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_name', models.CharField(max_length=30)),
                ('testimonial_location', models.CharField(max_length=50)),
                ('testimonial_image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('user_image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('about_me', models.TextField()),
            ],
        ),
    ]
