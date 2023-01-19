from django.shortcuts import render
from .form import ArticlesForm
from .models import User
from django.http import HttpResponse


# Create your views here.
# производим проверку и работа с данными
def User_index(request): #request ДОЛЖЕН БЫТЬ POST!
    error = ''
    if request.method == "POST":  # проверка на добавление
        print(request.POST)
        form = ArticlesForm(request.POST)  # получение данных с формы
        if form.is_valid():  # провека навалидность
           print(form.cleaned_data)
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

    data = {  # словарь который отправляем как ответ
        'form': form,
        'error': error
    }
    return render(request, 'djangoProject/user.html', data)

