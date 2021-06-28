from django.db import models

# Create your models here.


class Work(models.Model):
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    category = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
