
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('work', views.work, name='work'),
    path('contact', views.contact, name='contact'),
    path('verify', views.verify, name='verify'),
]
