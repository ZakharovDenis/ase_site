from django import forms
from ase_site.data.models import Application
from .widget import SelectTimeWidget


class MakeRequestForm(forms.ModelForm):
    delivery_date = forms.DateField(label='Дата Поставки', widget=forms.SelectDateWidget())
    delivery_time = forms.TimeField(label='Время Поставки', widget=SelectTimeWidget())
    class Meta():
        model = Application
        exclude = (
            'application_type',
            'status',
            'application_sender',
            'application_receiver',
            'delivery_date',
            'delivery_time'
        )