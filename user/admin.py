from django.contrib import admin, messages
from .models import *


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['surname','name', 'patronymic', 'self_phone_number','home_phone_number','passport_number']
    ordering = ['surname']
    list_per_page = 5
    search_fields = ['surname','name','patronymic','self_phone_number','home_phone_number','passport_number']
    list_filter = ['name','surname', 'patronymic']