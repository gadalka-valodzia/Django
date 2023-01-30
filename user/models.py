from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class User(models.Model):
    class Meta:
        verbose_name = 'Линые данные'
        verbose_name_plural = 'Личные данные'
    name = models.CharField(max_length=40,verbose_name='Имя')  # имя сотрудника
    surname = models.CharField(max_length=40,verbose_name='Фамилия')  # фамилия сотрудника
    patronymic = models.CharField(max_length=40,verbose_name='Отчество')  # отчество сотрудника
    self_phone_number = models.IntegerField(blank=True,verbose_name='Мобильный номер')  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField(blank=True,verbose_name='Домашний номер')  # номер городского телефона сотрудника
    passport_number = models.IntegerField(verbose_name='Номер паспорта')  # номер паспорта
    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
class list_promotion(models.Model):
    class Meta:
        verbose_name = 'Список поощерений'
        verbose_name_plural = 'Список поощерений'
    name_promotion = models.CharField(max_length=40,verbose_name='Поощрение')
    def __str__(self):
        return f'{self.name_promotion}'
class Promotion(models.Model):
    class Meta:
        verbose_name = 'Поощерения'
        verbose_name_plural = 'Поощерения'
    promotion = models.ForeignKey(list_promotion,on_delete=models.SET_NULL,null=True,verbose_name='Поощрение')
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'{self.promotion}'

class list_mecto(models.Model):
    class Meta:
        verbose_name = 'Список в/ч'
        verbose_name_plural = 'Список в/ч'
    name_mecto = models.CharField(max_length=40,verbose_name='Место работы')
    def __str__(self):
        return f'{self.name_mecto}'

class List_dolzhnost(models.Model):
    class Meta:
        verbose_name = 'Список должностей'
        verbose_name_plural = 'Список должностей'
    name_dolzhnost = models.CharField(max_length=40,verbose_name='Наименование должности')
    def __str__(self):
        return f'{self.name_dolzhnost}'

class Work(models.Model):
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работа'
    mesto = models.ForeignKey(list_mecto, on_delete=models.SET_NULL, null=True,verbose_name='Место работы')
    data_start_work = models.DateField(null=True,verbose_name='Дата начала')
    data_end_work = models.DateField(null=True,verbose_name='Дата окончания')
    dolzhnost = models.ForeignKey(List_dolzhnost, on_delete=models.SET_NULL, null=True,verbose_name='Должность')
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.mesto} {self.data_start_work} {self.data_end_work} {self.dolzhnost}'
class Contract(models.Model):
    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракт'
    data_zukluchenie = models.DateField(null=True,verbose_name='Дата заключения')
    data_okonchanie = models.DateField(null=True,verbose_name='Дата окончания')
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.data_zukluchenie} - {self.data_okonchanie}'

class Zvanie(models.Model):
    class Meta:
        verbose_name = 'Звания'
        verbose_name_plural = 'Звания'
    data_get = models.DateField(null=True,verbose_name='Дата получения')
    name_doc = models.CharField(max_length=40,verbose_name='Название документа')
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'{self.data_get} - {self.name_doc}'

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



class vid_Vziskanie(models.Model):

    class Meta:
        verbose_name = 'Вид взыскания'
        verbose_name_plural = 'Виды взысканий'

    name_vziskanie = models.CharField(max_length=40, verbose_name='Наименование',blank=True)

    def __str__(self):
        return f'{self.name_vziskanie}'


class Vziskanie(models.Model):
    class Meta:
        verbose_name = 'Взыскание'
        verbose_name_plural = 'Взыскания'

    vid_vziskania = models.OneToOneField(vid_Vziskanie,null=True, max_length=40, on_delete=models.SET_NULL,verbose_name='Вид взыскания',blank=True)
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.vid_vziskania}'