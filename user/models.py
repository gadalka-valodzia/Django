from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)  # имя сотрудника
    surname = models.CharField(max_length=40)  # фамилия сотрудника
    patronymic = models.CharField(max_length=40)  # отчество сотрудника
    self_phone_number = models.IntegerField()  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField()  # номер городского телефона сотрудника
    passport_number = models.IntegerField()  # номер паспорта
