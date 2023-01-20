from django.forms import ModelForm, TextInput
from .models import Promotion


class PromotionForm(ModelForm):
    class Meta:
        model = Promotion  # поля пользователя
        fields = ['promotion']
        exclude = ['personal_id']

        widgets = {  # как выглядят поля на HTML странице
            "promotion": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид поощерения'
            })
        }

