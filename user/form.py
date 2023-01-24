from django.forms import ModelForm, TextInput, Textarea
from .models import User
from .models import Promotion, Contract


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