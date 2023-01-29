from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)  # имя сотрудника
    surname = models.CharField(max_length=40)  # фамилия сотрудника
    patronymic = models.CharField(max_length=40)  # отчество сотрудника
    self_phone_number = models.IntegerField(blank=True)  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField(blank=True)  # номер городского телефона сотрудника
    passport_number = models.IntegerField()  # номер паспорта



class list_promotion(models.Model):
    name_promotion = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name_promotion}'
class Promotion(models.Model):
    promotion = models.ForeignKey(list_promotion,on_delete=models.SET_NULL,null=True)
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f'{self.promotion}'




class list_mecto(models.Model):
    name_mecto = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name_mecto}'

class List_dolzhnost(models.Model):
    name_dolzhnost = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.name_dolzhnost}'

class Work(models.Model):
    mesto = models.ForeignKey(list_mecto, on_delete=models.SET_NULL, null=True)
    data_start_work = models.DateField(null=True)
    data_end_work = models.DateField(null=True)
    dolzhnost = models.ForeignKey(List_dolzhnost, on_delete=models.SET_NULL, null=True)
    personal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Contract(models.Model):
    data_zukluchenie = models.DateField(null=True)
    data_okonchanie = models.DateField(null=True)
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.data_zukluchenie} - {self.data_okonchanie}'

class Zvanie(models.Model):
    data_get = models.DateField(null=True)
    name_doc = models.CharField(max_length=40)
    personal = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
