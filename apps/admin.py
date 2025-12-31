from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = 'full_name', 'email', 'phone_number', 'company'
    list_filter = 'email', 'phone_number', 'company'