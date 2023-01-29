from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class User(models.Model):
    class Meta:
        verbose_name = 'Линые данные'
        verbose_name_plural = 'Личные данные'
    name = models.CharField(max_length=40)  # имя сотрудника
    surname = models.CharField(max_length=40)  # фамилия сотрудника
    patronymic = models.CharField(max_length=40)  # отчество сотрудника
    self_phone_number = models.IntegerField(blank=True)  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField(blank=True)  # номер городского телефона сотрудника
    passport_number = models.IntegerField()  # номер паспорта

class list_promotion(models.Model):
    class Meta:
        verbose_name = 'Список поощерений'
        verbose_name_plural = 'Список поощерений'
    name_promotion = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name_promotion}'
class Promotion(models.Model):
    class Meta:
        verbose_name = 'Поощерения'
        verbose_name_plural = 'Поощерения'
    promotion = models.ForeignKey(list_promotion,on_delete=models.SET_NULL,null=True)
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'{self.promotion}'

class list_mecto(models.Model):
    class Meta:
        verbose_name = 'Список в/ч'
        verbose_name_plural = 'Список в/ч'
    name_mecto = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name_mecto}'

class List_dolzhnost(models.Model):
    class Meta:
        verbose_name = 'Список должностей'
        verbose_name_plural = 'Список должностей'
    name_dolzhnost = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name_dolzhnost}'

class Work(models.Model):
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работа'
    mesto = models.ForeignKey(list_mecto, on_delete=models.SET_NULL, null=True)
    data_start_work = models.DateField(null=True)
    data_end_work = models.DateField(null=True)
    dolzhnost = models.ForeignKey(List_dolzhnost, on_delete=models.SET_NULL, null=True)
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Contract(models.Model):
    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракт'
    data_zukluchenie = models.DateField(null=True)
    data_okonchanie = models.DateField(null=True)
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.data_zukluchenie} - {self.data_okonchanie}'

class Zvanie(models.Model):
    class Meta:
        verbose_name = 'Звания'
        verbose_name_plural = 'Звания'
    data_get = models.DateField(null=True)
    name_doc = models.CharField(max_length=40)
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

class vid_Rodstvenniki(models.Model):
    class Meta:
        verbose_name = 'Вид родственников'
        verbose_name_plural = 'Виды родтсвенников'

    name_rodstvennik = models.CharField(max_length=40, verbose_name='Наименование')

    def __str__(self):
        return f'{self.name_rodstvennik}'

class Rodstvenniki(models.Model):
    class Meta:
        verbose_name = 'Родственники'
        verbose_name_plural = 'Родственники'

    vid_svyazi = models.OneToOneField(vid_Rodstvenniki, null=True,on_delete=models.SET_NULL, verbose_name='Вид родственной связи',blank=True)
    name_rod = models.CharField(max_length=40, verbose_name='Имя')
    surname_rod = models.CharField(max_length=40, verbose_name='Фамилия')
    patronomyc_rod = models.CharField(max_length=40, verbose_name='Отчество')
    date_born = models.DateField(null=True, verbose_name='Дата рождения')
    date_brak = models.DateField(null=True, verbose_name='Дата брака')
    date_razvod = models.DateField(null=True, verbose_name='Дата развода')
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.surname_rod} {self.name_rod} {self.patronomyc}'


class vid_Zavedenie(models.Model):
    class Meta:
        verbose_name = 'Название УЗ'
        verbose_name_plural = 'Названия УЗ'

    name_vuz = models.CharField(max_length=40, verbose_name='Название')

    def __str__(self):
        return f'{self.name_vuz}'


class Obrazovanie(models.Model):
    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'

    vuz = models.OneToOneField(vid_Zavedenie, null=True, on_delete=models.SET_NULL, verbose_name='Наименования УЗ', blank=True)
    date_postuplen = models.DateField(null=True, verbose_name='Дата поступления')
    date_okonch = models.DateField(null=True, verbose_name='Дата окончания')
    obrazovanie_perepodgotovka = models.CharField(max_length=40, verbose_name='Образование/Переподготовка')
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.vuz}'
