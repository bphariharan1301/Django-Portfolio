# Generated by Django 3.2.4 on 2021-09-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20210921_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='live_at',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
