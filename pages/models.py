from django.db import models

# Create your models here.


# Create it after installing cloudinary in heroku add-on
class Work(models.Model):
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    category = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# class User(models.Model):
#     name = models.CharField(max_length=30)
#     user_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     about_me = models.TextField()

#     def __str__(self):
#         return self.name

# Create after Installing Cloudinary in heroku add-on
'''class Testimonail(models.Model):
    testimonial_name = models.CharField(max_length=30)
    testimonial_location = models.CharField(max_length=50)
    testimonial_image = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.testimonial_name
'''


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
