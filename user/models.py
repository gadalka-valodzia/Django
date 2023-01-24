from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.



class User(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    name = models.CharField(max_length=40,verbose_name='Имя')  # имя сотрудника
    surname = models.CharField(max_length=40,verbose_name='Фамилия')  # фамилия сотрудника
    patronymic = models.CharField(max_length=40,verbose_name='Отчество')  # отчество сотрудника
    self_phone_number = models.IntegerField(blank=True,verbose_name='Личный номер телефона')  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField(blank=True,verbose_name='Домашний телефон')  # номер городского телефона сотрудника
    passport_number = models.IntegerField(verbose_name='Номер паспорта')  # номер паспорта

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} '


class Contract(models.Model):
    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
    data_zukluchenie = models.DateField(null=True,verbose_name='Дата заключения')
    data_okonchanie = models.DateField(null=True,verbose_name='Дата окончания')
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.data_zukluchenie} - {self.data_okonchanie} - {self.personal}'
class Promotion(models.Model):
    class Meta:
        verbose_name = 'Поощрение'
        verbose_name_plural = 'Поощрения'
    promotion = models.CharField(max_length=40, verbose_name='Поощрение')
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.promotion}'