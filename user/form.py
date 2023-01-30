from django.forms import ModelForm, TextInput, Textarea
from .models import User
from .models import Promotion, Contract,Work,list_mecto, List_dolzhnost, list_promotion,Rodstvenniki,vid_Rodstvenniki,Obrazovanie,vid_Zavedenie,vid_Vziskanie


class UserForm(ModelForm):
    class Meta:
        model = User  # поля пользователя
        fields = ['name', 'surname', 'patronymic', 'self_phone_number', 'home_phone_number', 'passport_number']

        widgets = {  # как выглядят поля на HTML странице
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше отчество'
            }),
            "self_phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш мобильный номер телефона',
                'value': '+375'
            }),
            "home_phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш городской номер телефона',
                'value': '+375'
            }),
            "passport_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш номер паспорта'
            })
        }

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['data_okonchanie','data_zukluchenie']
        widgets = {
            "data_zukluchenie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заключения контракта',
                'id':'data',
                'type': 'date',
                'value': '2023-01-01'
            }),
            "data_okonchanie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания контракта',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            })
        }

class WorkForm(ModelForm):


    class Meta:
        model = Work
        fields = {'data_start_work','data_end_work'}
        widgets = {
            "data_start_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала работы',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            }),
            "data_end_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания работы',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            })
        }

class Mesto_nameForm(ModelForm):

    class Meta:
        model = list_mecto
        fields = {'name_mecto'}
        widgets = {
            "name_mecto": TextInput(attrs={
                'class': 'RadioSelect',
                'choices': 'CHOICES'
            })
        }

class Dolzhnosti_nameFrom(ModelForm):

    class Meta:
        model = List_dolzhnost
        fields = {'name_dolzhnost'}
        widgets = {
            "name_dolzhnost":TextInput(attrs={
                'class': 'RadioSelect',
                'choices': 'CHOICES'
        })
        }

class Promotion_nameForm(ModelForm):

    class Meta:
        model = list_promotion
        fields = {'name_promotion'}
        widgets = {
            "name_promotion":TextInput(attrs={
                'class': 'RadioSelect',
                'choices': 'CHOICES'
        })
        }

class RodstvennikiForm(ModelForm):
    class Meta:
        model = Rodstvenniki
        fields = ['name_rod','surname_rod','patronomyc_rod','date_born','date_brak','date_razvod']
        widgets = {
            "name_rod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),"surname_rod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "patronomyc_rod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "date_born": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            }),
            "date_brak": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата брака',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            }),
            "date_razvod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата развода',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            })
        }
class vid_RodstvennikiForm(ModelForm):
    class Meta:
        model = vid_Rodstvenniki
        fields = ['name_rodstvennik']
        widgets = {
            "name_rodstvennik": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид родственной связи'
            })
        }

class ObrazovanieForm(ModelForm):
    class Meta:
        model = Obrazovanie
        fields = ['date_postuplen','date_okonch','obrazovanie_perepodgotovka']
        widgets = {
            "date_postuplen": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата поступления',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            }),
            "date_okonch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания',
                'id': 'data',
                'type': 'date',
                'value': '2023-01-01'
            }),
            "obrazovanie_perepodgotovka": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Образование/переподготовка'
            })
        }

class vid_ZavedenieForm(ModelForm):
    class Meta:
        model = vid_Zavedenie
        fields = ['name_vuz']
        widgets = {
            "name_vuz": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование УЗ'
            })
        }


class vid_VziskanieForm(ModelForm):

    class Meta:
        model = vid_Vziskanie
        fields = ['name_vziskanie']
        widgets = {
            "name_vziskanie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид взыскания'

            })
        }
