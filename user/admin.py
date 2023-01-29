from django.contrib import admin, messages
from .models import *
from django.contrib.admin.models import LogEntry

# Register your models here.
LogEntry.objects.all().delete()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']
    ordering = ['surname']
    list_per_page = 7
    search_fields = ['surname', 'name', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']
    list_filter = ['name', 'surname', 'patronymic']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['personal', 'data_zukluchenie', 'data_okonchanie']
    ordering = ['personal']
    list_per_page = 7


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['promotion', 'personal']
    ordering = ['promotion']
    list_per_page = 7
    search_fields = ['promotion', 'personal']


@admin.register(Vziskanie)
class VziskanieAdmin(admin.ModelAdmin):
    list_display = ['vid_vziskania', 'personal']
    ordering = ['vid_vziskania']
    list_per_page = 7
    search_fields = ['vid_vziskania', 'personal']


@admin.register(vid_Vziskanie)
class vid_VziskanieAdmin(admin.ModelAdmin):
    list_display = ['name_vziskanie']
    ordering = ['name_vziskanie']
    list_per_page = 7
    search_fields = ['name_vziskanie']


@admin.register(Rodstvenniki)
class RodstvennikiAdmin(admin.ModelAdmin):
    list_display = ['vid_svyazi', 'personal','surname_rod','name_rod','patronomyc','date_born','date_brak','date_razvod']
    ordering = ['vid_svyazi']
    list_per_page = 7
    search_fields = ['vid_svyazi', 'personal']


@admin.register(vid_Rodstvenniki)
class vid_RodstvennikiAdmin(admin.ModelAdmin):
    list_display = ['name_rodstvennik']
    ordering = ['name_rodstvennik']
    list_per_page = 7
    search_fields = ['name_rodstvennik']


@admin.register(Obrazovanie)
class ObrazovanieAdmin(admin.ModelAdmin):
    list_display = ['vuz', 'personal','date_postuplen','date_okonch','obrazovanie_perepodgotovka']
    ordering = ['vuz']
    list_per_page = 7
    search_fields = ['vuz', 'personal']
@admin.register(vid_Zavedenie)
class vid_ZavedenieAdmin(admin.ModelAdmin):
    list_display = ['name_vuz']
    ordering = ['name_vuz']
    list_per_page = 7
    search_fields = ['name_vuz']
