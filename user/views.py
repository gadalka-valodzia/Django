from django.shortcuts import render
from .form import UserForm, PromotionForm, ContractForm,WorkForm,Mesto_nameForm
from .models import User, Promotion, Contract, Work, list_mecto
from django.http import HttpResponse


# Create your views here.
# производим проверку и работа с данными
def User_index(request):  # request ДОЛЖЕН БЫТЬ POST!
    error = ''
    if request.method == "POST":  # проверка на добавление
        print(request.POST)
        form = UserForm(request.POST)  # получение данных с формы
        form_promotion = PromotionForm(request.POST)
        form_contract = ContractForm(request.POST)
        form_work = WorkForm(request.POST)
        if form.is_valid() and form_promotion.is_valid() and form_contract.is_valid() and form_work.is_valid()  :  # провека навалидность
            print(form.cleaned_data)
            print(form_promotion.cleaned_data)
            print(form_contract.cleaned_data)
            print(form_work.cleaned_data)
            user_create = User(  # создание обьекта класса и занесение данных в бд
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                self_phone_number=form.cleaned_data['self_phone_number'],
                home_phone_number=form.cleaned_data['home_phone_number'],
                patronymic=form.cleaned_data['patronymic'],
                passport_number=form.cleaned_data['passport_number']
            )
            user_create.save()

            contract_create = Contract(
                data_zukluchenie=form_contract.cleaned_data['data_zukluchenie'],
                data_okonchanie=form_contract.cleaned_data['data_okonchanie'],
                personal_id=user_create.id
                        )
            contract_create.save()  # сохраняем данные в бд

            promotion_create = Promotion(
                promotion=form_promotion.cleaned_data['promotion'],
                personal_id=user_create.id
            )
            promotion_create.save()  # сохраняем данные в бд

            work_create = Work(
                mesto = form_work.cleaned_data['mesto'],
                data_start_work = form_work.cleaned_data['data_start_work'],
                data_end_work = form_work.cleaned_data['data_end_work'],
                dolzhnost = form_work.cleaned_data['dolzhnost'],
                personal_id = user_create.id
            )
            work_create.save()


             # сохраняем данные в бд
        else:
            error = 'Форма была заполнена неверно'


    form = UserForm()  # шаблон формы для передачи
    form_promotion = PromotionForm()
    form_contract = ContractForm()
    form_work = WorkForm()
    form_work_name = Mesto_nameForm()
    mesto=list_mecto.objects.all()
    data = dict(form=form, form_promotion=form_promotion, form_contract=form_contract, form_work=form_work,
            form_work_name=form_work_name, mesto=mesto, error=error)
    return render(request, 'djangoProject/user.html', data)
