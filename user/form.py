from django.forms import ModelForm, TextInput, Textarea
from .models import User
from .models import Promotion, Contract,Work,list_mecto, List_dolzhnost, list_promotion


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

class WorkForm(ModelForm):


    class Meta:
        model = Work
        fields = {'data_start_work','data_end_work'}
        widgets = {
            "data_start_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала работы'
            }),
            "data_end_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания работы'
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
