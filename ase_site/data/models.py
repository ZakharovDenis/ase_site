from django.db import models

from .choises import STATUS, TYPE, DELIVERY


class Company(models.Model):
    name = models.CharField('Название организации', primary_key=True, max_length=100)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


class GPS(models.Model):
    id = models.IntegerField('ИД Датчика', primary_key=True, editable=True)

    class Meta:
        verbose_name = 'ИД Датчика'
        verbose_name_plural = 'ИД Датчиков'

    def __str__(self):
        return str(self.id)


class CarType(models.Model):
    id = models.AutoField('ИД Машины', primary_key=True, editable=False)
    car_type = models.CharField('Тип Машины', max_length=120)

    class Meta:
        verbose_name = 'Тип Машины'
        verbose_name_plural = 'Типы Машин'

    def __str__(self):
        return str(self.car_type)


class Application(models.Model):
    from ase_site.auth_core.models import User

    application_type = models.IntegerField('Тип Заявки', choices=TYPE)
    status = models.IntegerField("Стадия заявки", choices=STATUS)

    density = models.FloatField('Плотность материала')
    delivery_place = models.CharField('Место выгрузки материала', max_length=120, default='')
    delivery_date = models.DateField('Дата Поставки')
    delivery_time = models.TimeField('Время Поставки')
    volume = models.FloatField('Объем(м^3)')

    project_number = models.CharField('Номер объекта', max_length=120, null=True, blank=True)
    material_class = models.CharField('Класс(марка)', max_length=20, null=True, blank=True)
    antifreeze = models.CharField('Противоморозная добавка', max_length=30, null=True, blank=True)
    water_resist = models.IntegerField('Водонепроницаемость', null=True, blank=True)
    freeze_resist = models.IntegerField('Морозостойкость', null=True, blank=True)
    ok = models.CharField('О-К', max_length=20, null=True, blank=True)
    lay_type = models.CharField('Способ укладки', max_length=20, null=True, blank=True)
    delivery_type = models.IntegerField('Доставка', choices=DELIVERY, null=True, blank=True)

    car = models.ForeignKey(CarType, on_delete=models.DO_NOTHING, verbose_name='Машина', related_name="carcar")
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
        User, on_delete=models.DO_NOTHING, verbose_name='Заявку Принял', related_name='application_receiver', null=True,
        blank=True
    )
    ocr_specialist = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Специалист ОСР', related_name='ocr_specialist', null=True,
        blank=False
    )

    disapprove_comment = models.TextField("Комментарий", null=True, blank=True)

    compile_date = models.DateField("Дата прибытия", null=True, blank=True)
    compile_time = models.TimeField("Время прибытия", null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Car(models.Model):
    car_number = models.CharField("Номер машины", primary_key=True, editable=True, max_length=15)
    car_type = models.ForeignKey(CarType, on_delete=models.DO_NOTHING, verbose_name="Тип машины")
    gps = models.ForeignKey(GPS, on_delete=models.DO_NOTHING, verbose_name='ИД Датчика')
    connected_application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,
                                              related_name='connected_application', blank=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return str(self.car_type)


class GPSdata(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_gps = models.ForeignKey(GPS, on_delete=models.DO_NOTHING)
    date = models.DateTimeField('Дата/время', editable=True, auto_now_add=True)
    latitude = models.CharField('Широта', editable=True, blank=False, max_length=50)
    longitude = models.CharField('Долгота', editable=True, blank=False, max_length=50)

    class Meta:
        verbose_name = 'Данные Датчика'
        verbose_name_plural = 'Данные Датчиков'

    def __str__(self):
        return str((float(self.latitude), float(self.longitude)))

    def get_tuple(self):
        return (self.latitude, self.longitude)
