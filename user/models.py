from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Promotion(models.Model):
    promotion = models.CharField(max_length=40)
    personal_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.promotion}'


class Contract(models.Model):
    data_zukluchenie = models.DateField(null=True)
    data_okonchanie = models.DateField(null=True)
    personal_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.personal_id} - {self.data_zukluchenie} - {self.data_okonchanie}'


class User(models.Model):
    name = models.CharField(max_length=40)  # имя сотрудника
    surname = models.CharField(max_length=40)  # фамилия сотрудника
    patronymic = models.CharField(max_length=40)  # отчество сотрудника
    self_phone_number = models.IntegerField(blank=True)  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField(blank=True)  # номер городского телефона сотрудника
    passport_number = models.IntegerField()  # номер паспорта

    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL,null=True)
