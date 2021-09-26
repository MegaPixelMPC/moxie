from .models import Leads
from django.forms import ModelForm, TextInput, Textarea, DateInput


class LeadsForm(ModelForm):
    class Meta:
        model = Leads
        fields = ["title", "name", "city", "description", "date"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Название инициативы'
            }),
            "name": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'ФИО'
            }),
            "city": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Город/Район/Регион'
            }),
            "description": Textarea(attrs={
                'class': 'area_input',
                'placeholder': 'Описание инициативы'
            }),
            "date": DateInput(attrs={
                'class': 'form_input',
                'placeholder': 'дд.мм.гг'
            })
        }