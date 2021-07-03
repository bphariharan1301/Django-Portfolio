from django.forms import fields, widgets
from pages.models import Contact
from django import forms

from django.core import validators
# from django.core.validators import EmailValidator


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ('name', 'email', 'subject', 'phone_number', 'message')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'text-input name-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'text-input email-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'text-input subject-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'text-input phone-inputt'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'text-input message-input'}),
        }
