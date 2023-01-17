from django.forms import ModelForm,TextInput,Textarea
from .models import User

class ArticlesForm(ModelForm):
    class Meta:
        model = User                            # поля пользователя
        fields = ['name','surname','patronymic','self_phone_number','home_phone_number','passport_number']

        widgets={                               # как выглядят поля на HTML странице
            "name":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ваше имя'
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
        }