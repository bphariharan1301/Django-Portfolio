
from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import *

# Register your models here.

admin.site.register(Work)
# admin.site.register(User)
admin.site.register(Testimonail)
admin.site.register(Technical_Skill)

class ContactAdmin(ExportActionMixin, admin.ModelAdmin):
  list_display = ('name', 'email', 'subject', 'phone_number', 'message')

# class BookAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('title', 'description', 'author', 'year')

admin.site.register(Contact, ContactAdmin)
