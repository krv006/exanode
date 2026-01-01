from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Contact, TelegramBot, ContactUs


@admin.register(ContactUs)
class ContactAdmin(ModelAdmin):
    list_display = 'full_name', 'email', 'phone_number', 'company'
    list_filter = 'email', 'phone_number', 'company'


@admin.register(TelegramBot)
class TelegramBotAdmin(ModelAdmin):
    pass


@admin.register(Contact)
class ContactBotAdmin(ModelAdmin):
    pass
