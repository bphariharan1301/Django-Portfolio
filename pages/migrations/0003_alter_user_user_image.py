# Generated by Django 3.2.4 on 2021-06-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_testimonails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]