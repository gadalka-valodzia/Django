from django.shortcuts import render
from  promotion.models import Promotion
# Create your views here.
def Promotion_save(form):
    promotion_create = Promotion(  # создание обьекта класса и занесение данных в бд
        promotion=form.cleaned_data['promotion'],
    )
    promotion_create.save()  # сохраняем данные в бд