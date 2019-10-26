from django import forms
from ase_site.data.models import Application


class MakeRequestForm(forms.ModelForm):
    class Meta():
        model = Application
        exclude = (
            'application_type',
            'status',
            'application_sender',
            # 'application_receiver'
        )


class MakeApplicationForm(forms.ModelForm):
    density = forms.FloatField('Плотность материала')
    volume = forms.FloatField('Объем')
    delivery_date = forms.DateField(label='Дата Поставки', widget=forms.SelectDateWidget())
    delivery_time = forms.TimeField(label='Время Поставки')
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, verbose_name='Машина')
    manufacturer_org = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, verbose_name='Организация Изготовитель', related_name='manufacturer_org'
    )
    performing_org = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, verbose_name='Организация Исполнитель', related_name='performing_org'
    )
    application_sender = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Заявитель', related_name='application_sender'
    )
    application_receiver = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Заявку Принял', related_name='application_receiver'
    )
    ocr_specialist