
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('work', views.work, name='work'),
    path('contact', views.contact, name='contact'),
    path('verify', views.verify, name='verify'),
    # path('verify', views.contact_verify, name='contact_verify'),
    # path('success', views.contact, name='success'),
]
