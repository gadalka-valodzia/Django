from django.forms import ModelForm, TextInput, Textarea
from .models import User
from .models import Promotion, Contract, Vziskanie, Obrazovanie,Rodstvenniki, vid_Rodstvenniki,vid_Vziskanie,vid_Zavedenie
from django import forms

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
                'placeholder': 'Ваш мобильный номер телефона'
            }),
            "home_phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш городской номер телефона'
            }),
            "passport_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш номер паспорта'
            })
            # "promotion": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Ваше поощерение'
            # })
        }

class PromotionForm(ModelForm):

    class Meta:
        model = Promotion
        fields = ['promotion']
        widgets = {
            "promotion": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше поощерение'
            })
        }
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['data_okonchanie','data_zukluchenie']
        widgets = {
            "data_zukluchenie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заключения контракта'
            }),
            "data_okonchanie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания контракта'
            })
        }
class VziskanieForm(ModelForm):
    class Meta:
        model = Vziskanie
        fields = ['vid_vziskania']
        widgets = {
            "vid_vziskania": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид взыскания'
            })
        }
class ObrazovanieForm(ModelForm):
    class Meta:
        model = Obrazovanie
        fields = ['vuz','date_postuplen','date_okonch','obrazovanie_perepodgotovka']
        widgets = {
            "vuz": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование УЗ'
            }),
            "date_postuplen": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата поступления'
            }),
            "date_okonch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания'
            }),
            "obrazovanie_perepodgotovka": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Образование/переподготовка'
            })
        }
class RodstvennikiForm(ModelForm):
    class Meta:
        model = Rodstvenniki
        fields = ['vid_svyazi','name_rod','surname_rod','patronomyc','date_born','date_brak','date_razvod']
        widgets = {
            "vid_svyazi": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид связи'
            }),
            "name_rod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),"surname_rod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "patronomyc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "date_born": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            "date_brak": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата брака'
            }),
            "date_razvod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата развода'
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