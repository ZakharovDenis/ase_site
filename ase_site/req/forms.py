from django import forms
from ase_site.data.models import Application


class MakeRequestForm(forms.ModelForm):
    class Meta():
        model = Application
        exclude = ('date', 'status',)