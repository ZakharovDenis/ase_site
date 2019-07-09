from django import forms
from ase_site.req.models import SendRequest
from .choises import INST_TYPE,DELIVERY,OK_CHOISES

class MakeRequestForm(forms.ModelForm):
    class Meta():
        model=SendRequest
        exclude=('date',)