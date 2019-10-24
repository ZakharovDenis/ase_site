from django import forms
from ase_site.data.models import ApplicationForm


class MakeRequestForm(forms.ModelForm):
    class Meta():
        model = ApplicationForm
        exclude = ('date', 'status',)