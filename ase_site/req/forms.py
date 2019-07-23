from django import forms
from ase_site.req.models import SendRequest

class MakeRequestForm(forms.ModelForm):
    class Meta():
        model=SendRequest
        exclude=('date','status',)