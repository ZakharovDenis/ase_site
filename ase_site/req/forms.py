from django import forms
from ase_site.data.models import Application
from .widget import SelectTimeWidget


class MakeRequestForm(forms.ModelForm):
    # delivery_date = forms.DateField(label='Дата Поставки', widget=forms.SelectDateWidget())
    # delivery_time = forms.TimeField(
    #     label='Время Поставки', widget=SelectTimeWidget(
    #         twelve_hr=False,
    #         minute_step=5,
    #         use_seconds=False)
    # )
    # application_receiver = forms.ModelChoiceField(queryset=Usr)

    class Meta():
        model = Application
        exclude = (
            'application_type',
            'status',
            'application_sender',
            # 'application_receiver',
            'delivery_date',
            'delivery_time'
        )
