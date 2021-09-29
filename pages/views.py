from pages.forms import ContactForm
from django.conf import settings
from Portfolio_Website.settings import EMAIL_HOST_USER
from pages.models import *
from django.shortcuts import redirect, render, resolve_url
from django.core.mail import send_mail
from django import forms
from verify_email.email_handler import send_verification_email
import string
from random import choice

# Create your views here.


def home(request):

    return render(request, 'pages/index.html')


def about(request):
    skills = Technical_Skill.objects.all()

    context = {
        'skills': skills,
    }
    return render(request, 'pages/about.html', context)


def work(request):
    works = Work.objects.all()

    context = {
        'works': works,
    }

    return render(request, 'pages/work.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        contact.user_email = email

        # Contacted User
        '''send_mail(
            'THANK YOU',
            'Hey, Your Email has reached us. \n\nWe will get back to you soon',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )'''

        # if (send_mail):
        '''send_mail(
            subject,
            message + '\n\nSent by' + '\n\nName: ' + name +
            '\n\nEmail-id: ' + email + '\n\nPhone Number: ' + phone_number,
            EMAIL_HOST_USER,
            ['bphariharan1301@gmail.com'],
            fail_silently=False
        )'''
    return render(request, 'pages/contact.html')


def success(request):

    return render(request, 'success.html')


def verify(request):

    if request.method == 'POST':
        otp = request.POST['otp']
    else:
        chars = string.digits
        random = ''.join(choice(chars) for i in range(4))
        random_otp = int(random)
        send_mail(
            'RANDOM OTP',
            'The OTP is: '+random,
            EMAIL_HOST_USER,
            # [contact.user_email, ],
            ['t@gmail.com'],
            fail_silently=False,
        )

    return render(request, 'pages/verify.html')
