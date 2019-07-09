from django.db import models

class Company(models.Model):
    id = models.AutoField(('ИД организации'),primary_key=True,editable=False)
    name=models.CharField(('Название организации'),max_length=100)
    city=models.CharField(('Город организации'),max_length=50)
    INN=models.CharField(('ИНН'),max_length=30)

    class Meta:
        verbose_name='Организация'
        verbose_name_plural='Организации'
        ordering=('name',)

    def __str__(self):
        return str(self.name)


class Driver(models.Model):
    id = models.AutoField(('ИД водителя'),primary_key=True,editable=False)
    name=models.CharField(('Имя'),max_length=45)
    last_name=models.CharField(('Фамилия'),max_length=50)
    fathers_name=models.CharField(('Отчество'),max_length=50)
    phone_number=models.CharField(('Номер телефона'),max_length=15)
    org=models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='Организация')

    class Meta:
        verbose_name='Водитель'
        verbose_name_plural='Водители'
        ordering=('last_name','name','fathers_name')

    def __str__(self):
        return str(self.last_name)+' '+str(self.name)+' '+str(self.fathers_name)
    
class GPS(models.Model):
    id = models.IntegerField(('ИД датчика'),primary_key=True,editable=True)
    class Meta:
        verbose_name='ИД датчика'
        verbose_name_plural='ИД датчиков'

    def __str__(self):
        return str(self.id)

class GPSdata(models.Model):
    id = models.IntegerField(('ИД датчика'),primary_key=True,editable=False)
    date=models.DateTimeField('Дата/время',editable=False)
    latitude=models.CharField('Широта',editable=False,blank=False, max_length=50)
    longitude=models.CharField('Долгота',editable=False,blank=False, max_length=50)

    class Meta:
        verbose_name='Данные датчика'
        verbose_name_plural='Данные датчиков'

    def __str__(self):
        return str(id)

class Car(models.Model):
    id = models.AutoField(('ИД машины'),primary_key=True,editable=False)
    cartype=models.CharField(('Тип машины'),max_length=45)
    label=models.CharField(('Марка'),max_length=50)
    max_weight=models.IntegerField(('Грузоподьемность'))
    car_weigth=models.FloatField(('Вес машины'))
    driver=models.ForeignKey(Driver, on_delete=models.DO_NOTHING, verbose_name="Водитель")
    gps=models.ForeignKey(GPS,on_delete=models.DO_NOTHING, verbose_name='ИД датчика')
    
    class Meta:
        verbose_name='Машина'
        verbose_name_plural='Машины'

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    id = models.AutoField(('ИД доставки'), primary_key=True, editable=False)
    start_place = models.CharField(('Начальный пункт'), max_length=50)
    end_place = models.CharField(('Конечный пункт'), max_length=50)
    material_type = models.CharField(('Тип материала'),max_length=50)
    date = models.DateField(('Дата поставки'))
