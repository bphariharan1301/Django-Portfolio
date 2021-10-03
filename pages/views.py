from pages.forms import ContactForm
from django.conf import settings
from Portfolio_Website.settings import EMAIL_HOST_USER
from pages.models import *
from django.shortcuts import redirect, render
from django.core.mail import send_mail

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

        contact.user_name = name
        contact.user_email = email
        contact.user_subject = subject
        contact.user_phone_number = phone_number
        contact.user_message = message

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
        chars = string.digits
        random = ''.join(choice(chars) for i in range(4))
        random_otp = int(random)
        contact.user_otp = random_otp
        print(contact.user_otp)
        send_mail(
            'RANDOM OTP',
            'The OTP is: '+random,
            EMAIL_HOST_USER,
            [contact.user_email, ],
            # ['t@gmail.com'],
            fail_silently=False,
        )
        return redirect('verify')
    return render(request, 'pages/contact.html')


def success(request):

    return render(request, 'success.html')


def verify(request):
    # random_otp = 0
    if request.method == 'POST':
        otp = request.POST['otp']
        # print(contact.user_otp)
        print(otp)
        print(type(otp))
        user_otp = int(otp)
        if contact.user_otp == user_otp:
            print('OTP VERIFIED')
            send_mail(
                'THANK YOU',
                'Hey, Your Email has reached us. \n\nWe will get back to you soon',
                EMAIL_HOST_USER,
                [contact.user_email],
                fail_silently=False,
            )

            send_mail(
                contact.user_subject,
                contact.user_message + '\n\nSent by' + '\n\nName: ' + contact.user_name +
                '\n\nEmail-id: ' + contact.user_email +
                '\n\nPhone Number: ' + contact.user_phone_number,
                EMAIL_HOST_USER,
                ['bphariharan1301@gmail.com'],
                fail_silently=False
            )

            user_contact = Contact(name=contact.user_name, email=contact.user_email, subject=contact.user_subject,
                                   phone_number=contact.user_phone_number, message=contact.user_message)
            user_contact.save()

            return redirect('home')

    return render(request, 'pages/verify.html')
