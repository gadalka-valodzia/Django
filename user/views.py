from django.shortcuts import render
from .form import UserForm, PromotionForm, ContractForm, VziskanieForm, RodstvennikiForm, ObrazovanieForm, \
    vid_VziskanieForm, vid_RodstvennikiForm, vid_ZavedenieForm
from .models import User, Promotion, Contract, Vziskanie, Rodstvenniki, Obrazovanie, vid_Vziskanie, vid_Rodstvenniki, \
    vid_Zavedenie
from django.http import HttpResponse
from django.contrib import admin


# Create your views here.
# производим проверку и работа с данными
def User_index(request):  # request ДОЛЖЕН БЫТЬ POST!
    error = ''
    if request.method == "POST":  # проверка на добавление
        print(request.POST)
        form = UserForm(request.POST)  # получение данных с формы
        form_promotion = PromotionForm(request.POST)
        form_contract = ContractForm(request.POST)
        form_vziskanie = VziskanieForm(request.POST)
        form_rodstvenniki = RodstvennikiForm(request.POST)
        form_obrazovanie = ObrazovanieForm(request.POST)
        form_vid_vziskanie = vid_VziskanieForm(request.POST)
        form_vid_rodstvenniki = vid_RodstvennikiForm(request.POST)
        form_vid_zavedenie = vid_ZavedenieForm(request.POST)
        if form.is_valid() and form_promotion.is_valid() and form_contract.is_valid() and form_vid_zavedenie.is_valid() and form_vid_vziskanie.is_valid() and form_vid_rodstvenniki.is_valid() and form_vziskanie.is_valid() and form_rodstvenniki.is_valid() and form_obrazovanie.is_valid():  # провека навалидность
            print(form.cleaned_data)
            print(form_promotion.cleaned_data)
            print(form_contract.cleaned_data)
            print(form_vid_zavedenie.cleaned_data)
            print(form_vid_rodstvenniki.cleaned_data)
            print(form_vid_vziskanie.cleaned_data)
            print(form_obrazovanie.cleaned_data)
            print(form_rodstvenniki.cleaned_data)
            print (form_vziskanie.cleaned_data)
            user_create = User(  # создание обьекта класса и занесение данных в бд
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                self_phone_number=form.cleaned_data['self_phone_number'],
                home_phone_number=form.cleaned_data['home_phone_number'],
                patronymic=form.cleaned_data['patronymic'],
                passport_number=form.cleaned_data['passport_number']

            )
            user_create.save()  # сохраняем данные в бд
            promotion_create = Promotion(
                promotion=form_promotion.cleaned_data['promotion'],
                personal=user_create

            )
            promotion_create.save()  # сохраняем данные в бд
            contract_create = Contract(
                data_zukluchenie=form_contract.cleaned_data['data_zukluchenie'],
                data_okonchanie=form_contract.cleaned_data['data_okonchanie'],
                personal=user_create
            )
            contract_create.save()  # сохраняем данные в бд

            vid_vziskanie_create = vid_Vziskanie(
                name_vziskanie=form_vid_vziskanie.cleaned_data['name_vziskanie']
            )
            vid_vziskanie_create.save()

            vid_zavedenie_create = vid_Zavedenie(
                name_vuz=form_vid_zavedenie.cleaned_data['name_vuz']
            )
            vid_zavedenie_create.save()

            vid_rodstvenniki_create = vid_Rodstvenniki(
                name_rodstvennik=form_vid_rodstvenniki.cleaned_data['name_rodstvennik']
            )
            vid_rodstvenniki_create.save()

            vziskanie_create = Vziskanie(
                vid_vziskania=vid_vziskanie_create,
                personal=user_create
            )
            vziskanie_create.save()
            rodstvenniki_create = Rodstvenniki(
                personal=user_create,
                vid_svyazi=vid_rodstvenniki_create,
                name_rod=form_rodstvenniki.cleaned_data['name_rod'],
                surname_rod=form_rodstvenniki.cleaned_data['surname_rod'],
                patronomyc=form_rodstvenniki.cleaned_data['patronomyc'],
                date_born=form_rodstvenniki.cleaned_data['date_born'],
                date_brak=form_rodstvenniki.cleaned_data['date_brak'],
                date_razvod=form_rodstvenniki.cleaned_data['date_razvod'],
            )
            rodstvenniki_create.save()
            obrazovanie_create = Obrazovanie(
                personal=user_create,
                vuz=vid_zavedenie_create,
                date_postuplen=form_obrazovanie.cleaned_data['date_postuplen'],
                date_okonch=form_obrazovanie.cleaned_data['date_okonch'],
                obrazovanie_perepodgotovka=form_obrazovanie.cleaned_data['obrazovanie_perepodgotovka']

            )
            obrazovanie_create.save()


        else:
            error = 'Форма была заполнена неверно'

    else:

        form = UserForm()  # шаблон формы для передачи
        form_promotion = PromotionForm()
        form_contract = ContractForm()
        form_vziskanie = VziskanieForm()
        form_rodstvenniki = RodstvennikiForm()
        form_obrazovanie = ObrazovanieForm()
        form_vid_vziskanie = vid_VziskanieForm()
        form_vid_rodstvenniki = vid_RodstvennikiForm()
        form_vid_zavedenie = vid_ZavedenieForm()

    data = {  # словарь который отправляем как ответ
        'form': form,
        'form_promotion': form_promotion,
        'form_contract': form_contract,
        'form_vziskanie': form_vziskanie,
        'form_rodstvenniki': form_rodstvenniki,
        'form_obrazovanie': form_obrazovanie,
        'form_vid_vziskanie': form_vid_vziskanie,
        'form_vid_rodstvenniki': form_vid_rodstvenniki,
        'form_vid_zavedenie': form_vid_zavedenie,
        'error': error
    }
    return render(request, 'djangoProject/user.html', data)
def FAQ_index(request):
    return render(request,"djangoProject/faq.html")
def Main_index(request):
    return render(request, "djangoProject/base.html")
def Test_index(request):
    return render(request,"djangoProject/index.html")