from django.db import models
from .choises import OK_CHOISES, INST_TYPE, DELIVERY, TYPE, STATUS

class SendRequest(models.Model):
    concrete_make_org=models.CharField(('Организация-изготовитель бетонной смеси'),max_length=120)
    maker_org=models.CharField(('Организация-исполнитель работ'),max_length=120)
    obj_name=models.CharField(('Наименование объекта'),max_length=120)
    proj_number=models.CharField(('Номер проекта'),max_length=120)
    supply_date=models.DateField(('Дата поставки'))
    supply_time=models.TimeField(('Время поставки'))
    value=models.FloatField(('Объем'))
    mark=models.CharField(('Класс (марка)'),max_length=10)
    anti_freeze=models.CharField(('Противоморозная добавкa'),max_length=10)
    water_resist=models.CharField(('Водонепроницаемость'),max_length=10)
    freeze_resist=models.CharField(('Морозостойкость'),max_length=10)
    o_k=models.IntegerField(('О-К'),choices=OK_CHOISES)
    install_type=models.IntegerField(('Способ укладки'),choices=INST_TYPE)
    responsible_person=models.CharField(('Ответственное лицо'),max_length=50)
    delivery=models.IntegerField(('Доставка'),choices=DELIVERY)
    req_sender=models.CharField(('Заявку передал'),max_length=120)
    req_resiver=models.CharField(('Заявку принял'),max_length=120)
    OSR_specialis=models.CharField(('Специалист ОСР'),max_length=120)
    date = models.DateField(auto_now_add=True, blank = False)
    status = models.IntegerField(default=3)
    req_type = models.IntegerField(('Материал'),choices=TYPE)

    class Meta:
        verbose_name='Запрос'
        verbose_name_plural='Запросы'


