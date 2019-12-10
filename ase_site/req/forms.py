from django import forms
from ase_site.data.models import Application
from .widget import SelectTimeWidget


class beton_form(forms.ModelForm):
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
    class Meta:
        model = Application
        exclude = (
            'application_type',
            'status',
            'application_sender',
            'application_receiver',
            'delivery_date',
            'delivery_time',
            'project_number',
            'material_class',
            'antifreeze',
            'water_resist',
            'freeze_resist',
            'ok',
            'lay_type',
            'delivery_type',
            'disapprove_comment',
            'compile_date',
            'compile_time',
        )