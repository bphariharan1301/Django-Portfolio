from pages.forms import ContactForm
from django.conf import settings
from Portfolio_Website.settings import EMAIL_HOST_USER
from pages.models import *
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django import forms
from verify_email.email_handler import send_verification_email


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

        # form = ContactForm(request.POST)
        # if form.is_valid():
        # # form.save()
        # name = form.cleaned_data['name']
        # email = form.cleaned_data['email']
        # subject = form.cleaned_data['subject']
        # phone_number = form.cleaned_data['phone_number']
        # message = form.cleaned_data['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone_number']
        message = request.POST['message']

        # Contacted User
        send_mail(
            'THANK YOU',
            'Hey, Your Email has reached us. \n\nWe will get back to you soon',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # if (send_mail):
        send_mail(
            subject,
            message + '\n\nSent by' + '\n\nName: ' + name +
            '\n\nEmail-id: ' + email + '\n\nPhone Number: ' + phone_number,
            EMAIL_HOST_USER,
            ['bphariharan1301@gmail.com'],
            fail_silently=False
        )
        # return render(request, 'contact/success.html')
        # form.save()
        # return render(request, 'partials/_success.html')
        # form = ContactForm()
        # context = {'form': form}
    return render(request, 'pages/contact.html')


def success(request):

    return render(request, 'success.html')
