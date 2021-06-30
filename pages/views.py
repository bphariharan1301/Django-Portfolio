from Portfolio_Website.settings import EMAIL_HOST_USER
from pages.models import Contact, Technical_Skill, Work, User
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

users = User.objects.all()


def home(request):
    context = {
        'users': users,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    skills = Technical_Skill.objects.all()

    context = {
        'users': users,
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
        subject = request.POST['subject']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject,
                          phone_number=phone_number, message=message)

        contact.save()
        # To the Contacted Person
        send_mail(
            'THANK YOU FOR GETTING IN TOUCH',  # subject,
            'Hey, ' + name + '\n\nHope you are doing good and having a fantastic day. Thank you for contacting me.' +
            '\n\n I will get back to you soon',  # message/body,
            EMAIL_HOST_USER,  # from,
            # To/Recieptents which is tuple ['email-1', 'email-2', ....., 'email-n'],
            [email],
            fail_silently=False,
        )

        # To yourself as a infomation
        send_mail(
            'NEW CONTACT',
            'You have been contacted by ' + name + ' for "' + subject +
            '". Details give below,' + '\n\n' + message + '\n\nHave a nice day',
            EMAIL_HOST_USER,
            ['bphariharan1301@gmail.com'],
            fail_silently=False,
        )

        return redirect('home')
    else:
        return render(request, 'pages/contact.html')
