from django import forms
from ase_site.data.models import Application
from .widget import SelectTimeWidget
from ase_site.auth_core.models import User


class beton_form(forms.ModelForm):
    ocr_specialist = forms.ModelChoiceField(
        queryset=User.objects.filter(level=3), 
        widget=forms.Select(), 
        label="Специалист ОСР",
        )

    class Meta():
        model = Application
        exclude = (
            'application_type',
            'status',
            'application_sender',
            'application_receiver',
            'delivery_date',
            'delivery_time',
            'disapprove_comment',
            'compile_date',
            'compile_time',
        )


class sand_pgs_form(forms.ModelForm):
    ocr_specialist = forms.ModelChoiceField(
        queryset=User.objects.filter(level=3), 
        widget=forms.Select(), 
        label="Специалист ОСР",
        )

    class Meta:
        model = Application
        exclude = (
            'application_type',
            'status',
            'application_sender',
            'application_receiver',
            'delivery_date',
            'delivery_time',
            'material_class',
            'antifreeze',
            'water_resist',
            'freeze_resist',
            'ok',
            'lay_type',
            'disapprove_comment',
            'compile_date',
            'compile_time',
        )