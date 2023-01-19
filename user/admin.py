from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'patronymic', 'self_phone_number']
    ordering = ['name']
    list_per_page = 5