from django.shortcuts import render
from .form import ArticlesForm
from django.http import HttpResponse
# Create your views here.
# произодим проверку и работа с данными
def User(request):
    error=''
    if request.method == "POST":                    #проверка на добавление
        form = ArticlesForm(request.POST)           #получение данных с формы
        if form.is_valid():                         #провека навалидность
            form.save()                             #сохраняем данные
        else:
            error = 'Форма была заполнена неверно'

    form = ArticlesForm()                           #шаблон формы для передачи

    data = {                                        # словарь который отправляем как ответ
        'form':form,
        'error':error
    }

    return render(request,'djangoProject/user.html',data)