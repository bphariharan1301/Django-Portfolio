from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


# Create it after installing cloudinary in heroku add-on
class Work(models.Model):
    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_main = CloudinaryField('work')
    category = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    live_at = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

# Create after Installing Cloudinary in heroku add-on
class Testimonail(models.Model):
    testimonial_name = models.CharField(max_length=30)
    testimonial_location = models.CharField(max_length=50)
    ''' testimonial_image = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True)'''
    testimonial_image = CloudinaryField('testimonial_image')

    def __str__(self):
        return self.testimonial_name


class Technical_Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    experience_level = models.IntegerField()

    def __str__(self):
        return self.skill_name


class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name
