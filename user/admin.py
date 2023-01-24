from django.contrib import admin, messages
from .models import *
from django.contrib.admin.models import LogEntry


# Register your models here.
LogEntry.objects.all().delete()
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']
    ordering = ['surname']
    list_per_page = 5
    search_fields = ['surname', 'name', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']
    list_filter = ['name', 'surname', 'patronymic']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['personal','data_zukluchenie', 'data_okonchanie']
    ordering = ['personal']
    list_per_page = 7

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['promotion','personal_id']
    ordering = ['promotion']
    list_per_page = 7
    search_fields = ['promotion','personal_id']
