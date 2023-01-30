from django.shortcuts import render
from .form import UserForm,  ContractForm,WorkForm,Mesto_nameForm, Dolzhnosti_nameFrom, Promotion_nameForm,vid_RodstvennikiForm,RodstvennikiForm,vid_ZavedenieForm,vid_VziskanieForm,ObrazovanieForm
from .models import User, Promotion, Contract, Work, list_mecto, List_dolzhnost, list_promotion,vid_Rodstvenniki,Rodstvenniki,vid_Zavedenie,Obrazovanie,vid_Vziskanie,Vziskanie
from django.http import HttpResponse


# Create your views here.
# производим проверку и работа с данными
def User_index(request):  # request ДОЛЖЕН БЫТЬ POST!
    error = ''
    if request.method == "POST":  # проверка на добавление
        print(request.POST)
        form = UserForm(request.POST)  # получение данных с формы
        form_contract = ContractForm(request.POST)
        form_work = WorkForm(request.POST)
        form_wotk_list = Mesto_nameForm(request.POST)
        form_dolzh_list = Dolzhnosti_nameFrom(request.POST)
        form_promotion_list = Promotion_nameForm(request.POST)
        form_name_rodstvennik = vid_RodstvennikiForm(request.POST)
        form_rodstvenniki = RodstvennikiForm(request.POST)
        form_obrazovanie = ObrazovanieForm(request.POST)
        form_vid_zavedenie = vid_ZavedenieForm(request.POST)
        form_vziskanie_list=vid_VziskanieForm(request.POST)
        if form.is_valid()  and form_obrazovanie.is_valid() and form_vziskanie_list.is_valid() and form_vid_zavedenie.is_valid() and form_contract.is_valid() and form_work.is_valid() and form_wotk_list.is_valid() and form_dolzh_list.is_valid() and form_rodstvenniki.is_valid() and form_promotion_list.is_valid() and form_name_rodstvennik.is_valid():  # провека навалидность
            print(form.cleaned_data)
            print(form_contract.cleaned_data)
            print(form_work.cleaned_data)
            print(form_wotk_list.cleaned_data)
            print(form_dolzh_list.cleaned_data)
            print(form_promotion_list.cleaned_data)
            print(form_rodstvenniki.cleaned_data)
            print(form_name_rodstvennik.cleaned_data)
            print(form_obrazovanie.cleaned_data)
            print(form_vid_zavedenie.cleaned_data)
            print(form_vziskanie_list.cleaned_data)
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
                promotion=list_promotion.objects.get(name_promotion=form_promotion_list.cleaned_data['name_promotion']),
                personal_id=user_create.id
            )
            promotion_create.save()  # сохраняем данные в бд

            work_create = Work(
                mesto = list_mecto.objects.get(name_mecto=form_wotk_list.cleaned_data['name_mecto']),
                data_start_work = form_work.cleaned_data['data_start_work'],
                data_end_work = form_work.cleaned_data['data_end_work'],
                dolzhnost = List_dolzhnost.objects.get(name_dolzhnost = form_dolzh_list.cleaned_data['name_dolzhnost']),
                personal_id = user_create.id
            )
            work_create.save()

            rodstvenniki_create = Rodstvenniki(
                personal=user_create,
                vid_svyazi=vid_Rodstvenniki.objects.get(name_rodstvennik=form_name_rodstvennik.cleaned_data['name_rodstvennik']),
                name_rod=form_rodstvenniki.cleaned_data['name_rod'],
                surname_rod=form_rodstvenniki.cleaned_data['surname_rod'],
                patronomyc_rod=form_rodstvenniki.cleaned_data['patronomyc_rod'],
                date_born=form_rodstvenniki.cleaned_data['date_born'],
                date_brak=form_rodstvenniki.cleaned_data['date_brak'],
                date_razvod=form_rodstvenniki.cleaned_data['date_razvod'],
            )
            rodstvenniki_create.save()

            obrazovanie_create = Obrazovanie(
                personal=user_create,
                vuz=vid_Zavedenie.objects.get(name_vuz=form_vid_zavedenie.cleaned_data['name_vuz']),
                date_postuplen=form_obrazovanie.cleaned_data['date_postuplen'],
                date_okonch=form_obrazovanie.cleaned_data['date_okonch'],
                obrazovanie_perepodgotovka=form_obrazovanie.cleaned_data['obrazovanie_perepodgotovka']

            )
            obrazovanie_create.save()

            vziskanie_create = Vziskanie(
                vid_vziskania=vid_Vziskanie.objects.get(name_vziskanie = form_vziskanie_list.cleaned_data['name_vziskanie']),
                personal=user_create
            )
            vziskanie_create.save()
             # сохраняем данные в бд
        else:
            error = 'Форма была заполнена неверно'


    form = UserForm()  # шаблон формы для передачи
    form_contract = ContractForm()
    form_work = WorkForm()
    form_work_name = Mesto_nameForm()
    form_rodstvenniki = RodstvennikiForm()
    form_zavedenie = ObrazovanieForm()
    mesto=list_mecto.objects.all()
    dolzhnocti_list=List_dolzhnost.objects.all()
    promotion_list = list_promotion.objects.all()
    vid_rod = vid_Rodstvenniki.objects.all()
    vid_zav = vid_Zavedenie.objects.all()
    vid_vzisk =vid_Vziskanie.objects.all()
    data = dict(form=form, form_contract=form_contract, form_work=form_work,form_obraz = form_zavedenie,vzisk=vid_vzisk,
            form_work_name=form_work_name, mesto=mesto,dolzhnost=dolzhnocti_list,vid_zaved = vid_zav,form_rodstvennik= form_rodstvenniki,promotion=promotion_list,rod=vid_rod, error=error)
    return render(request, 'djangoProject/user.html', data)

def FAQ_index(request):
    return render(request,"djangoProject/faq.html")
def Main_index(request):
    return render(request, "djangoProject/base.html")
def Test_index(request):
    return render(request,"djangoProject/index.html")