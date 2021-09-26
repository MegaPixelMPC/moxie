from .models import Events
from django.forms import ModelForm, TextInput, Textarea, DateInput


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ["title", "name", "city", "description", "date"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'Название мероприятия'
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
                'placeholder': 'Описание мероприятия'
            }),
            "date": DateInput(attrs={
                'class': 'form_input',
                'placeholder': 'дд.мм.гг'
            })
        }