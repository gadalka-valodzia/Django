from django.contrib import admin, messages
from .models import *


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']
    ordering = ['surname']
    list_per_page = 10
    search_fields = ['surname', 'name', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']
    list_filter = ['name', 'surname', 'patronymic']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['personal_id','data_zukluchenie', 'data_okonchanie']
    ordering = ['personal_id']
    list_per_page = 7
    list_filter = ['personal_id', 'data_zukluchenie', 'data_okonchanie']

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['promotion','personal_id']
    ordering = ['promotion']
    list_per_page = 7
    search_fields = ['promotion','personal_id']
    list_filter = ['promotion', 'personal_id']

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['personal','dolzhnost','mesto','data_start_work','data_end_work']
    ordering = ['personal']
    list_per_page = 5
    search_fields = ['personal']
    list_filter = ['personal','mesto','dolzhnost','personal_id']

@admin.register(list_mecto)
class MestoAdmit(admin.ModelAdmin):

    list_display = ['name_mecto']
    ordering = ['name_mecto']
    list_per_page = 9
    search_fields = ['name_mecto']
@admin.register(list_promotion)
class list_promotionAdmin(admin.ModelAdmin):

    list_display = ['name_promotion']
    ordering = ['name_promotion']
    list_per_page = 9
    search_fields = ['name_promotion']

@admin.register(List_dolzhnost)
class List_dolzhnostAdmin(admin.ModelAdmin):
    list_display = ['name_dolzhnost']
    ordering = ['name_dolzhnost']
    list_per_page = 5
    search_fields = ['name_dolzhnost']

@admin.register(Zvanie)
class ZvanieAdmin(admin.ModelAdmin):
    list_display = ['personal','data_get','name_doc']
    ordering = ['personal']
    list_per_page = 5
    search_fields = ['personal','data_get','name_doc']
    list_filter = ['personal','data_get','name_doc']

@admin.register(vid_Rodstvenniki)
class vid_RodstvennikiAdmin(admin.ModelAdmin):
    list_display = ['name_rodstvennik']
    ordering = ['name_rodstvennik']
    list_per_page = 5
    search_fields = ['name_rodstvennik']
    list_filter = ['name_rodstvennik']

@admin.register(Rodstvenniki)
class RodstvennikiAdmin(admin.ModelAdmin):
    list_display = ['personal','vid_svyazi', 'surname_rod','name_rod','patronomyc_rod', 'date_born','date_brak','date_razvod']
    ordering = ['personal']
    list_per_page = 5
    search_fields = ['personal','vid_svyazi', 'surname_rod','name_rod','patronomyc_rod', 'date_born','date_brak','date_razvod']
    list_filter = ['vid_svyazi']

@admin.register(vid_Zavedenie)
class vid_ZavedenieAdmin(admin.ModelAdmin):
    list_display = ['name_vuz']
    ordering = ['name_vuz']
    list_per_page = 5
    search_fields = ['name_vuz']
    list_filter = ['name_vuz']

@admin.register(Obrazovanie)
class ObrazovanieAdmin(admin.ModelAdmin):
    list_display = ['personal','vuz','date_postuplen','date_okonch','date_postuplen','obrazovanie_perepodgotovka']
    ordering = ['personal']
    list_per_page = 5
    search_fields = ['personal','vuz','date_postuplen','date_okonch','date_postuplen','obrazovanie_perepodgotovka']
    list_filter = ['personal','vuz','date_postuplen','date_okonch','date_postuplen','obrazovanie_perepodgotovka']

@admin.register(vid_Vziskanie)
class vid_VziskanieAdmin(admin.ModelAdmin):
    list_display = ['name_vziskanie']
    ordering = ['name_vziskanie']
    list_per_page = 5
    search_fields = ['name_vziskanie']
    list_filter = ['name_vziskanie']

@admin.register(Vziskanie)
class VziskanieAdmin(admin.ModelAdmin):
    list_display = ['personal','vid_vziskania']
    ordering = ['personal']
    list_per_page = 5
    search_fields = ['personal', 'vid_vziskania']
    list_filter = ['personal','vid_vziskania']