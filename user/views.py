from django.shortcuts import render
from .form import ArticlesForm
from .models import User
from promotion.form_promotion import PromotionForm
from promotion.views import Promotion_save
from django.http import HttpResponse


# Create your views here.
# производим проверку и работа с данными
def User_index(request): #request ДОЛЖЕН БЫТЬ POST!
    error = ''
    if request.method == "POST":  # проверка на добавление
        print(request.POST)
        form = ArticlesForm(request.POST)  # получение данных с формы
        form_promotion = PromotionForm(request.POST)
        if form.is_valid() and form_promotion.is_valid():  # провека навалидность
           print(form.cleaned_data)
           print(form_promotion.cleaned_data)
           Promotion_save(form_promotion)
           user_create = User(       # создание обьекта класса и занесение данных в бд
               name=form.cleaned_data['name'],
               surname=form.cleaned_data['surname'],
               self_phone_number=form.cleaned_data['self_phone_number'],
               home_phone_number=form.cleaned_data['home_phone_number'],
               patronymic=form.cleaned_data['patronymic'],
               passport_number=form.cleaned_data['passport_number']
           )
           user_create.save() #сохраняем данные в бд
        else:
            error = 'Форма была заполнена неверно'

    else:
        form = ArticlesForm()  # шаблон формы для передачи

    form_promotion = PromotionForm(request.POST)
    data = {  # словарь который отправляем как ответ
        'form': form,
        'form_promotion': form_promotion,
        'error': error
    }
    return render(request, 'djangoProject/user.html', data)

