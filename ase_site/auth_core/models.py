from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .choices import STATUS_CHOICES
from phonenumber_field.modelfields import PhoneNumberField
from ase_site.data.models import Company


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, active=False, staff=False, admin=False,first_name=None,last_name=None,fathers_name=None,firm_name=None,level=None):
        if not email:
            raise ValueError("Set email")
        if not password:
            raise ValueError("Set pass")
        user_obj=self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.is_active = active
        user_obj.is_staff = staff
        user_obj.is_admin = admin
        user_obj.first_name = first_name
        user_obj.firm_name = firm_name
        user_obj.last_name = last_name
        user_obj.fathers_name = fathers_name
        user_obj.level = level
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, active=True, staff=True, admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(('Электронная почта'),unique=True)
    first_name = models.CharField(('Имя'),max_length=30, blank=True, null=True)
    last_name = models.CharField(('Фамилия'),max_length=30, blank=True, null=True)
    fathers_name = models.CharField(('Отчетсво'),max_length=30, blank=True, null=True)
    phone  = PhoneNumberField(("Телефон"), blank=True, null=True, max_length=30)
    date_joined = models.DateTimeField(('Дата регистрации'), auto_now_add=True)
    is_active = models.BooleanField(('Активирован'), default=False)
    firm_name = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, verbose_name='Название', related_name='firm_name', null=True
    )
    level = models.IntegerField(('Статус сотрудника'), choices=STATUS_CHOICES, blank=True, null=True)
    is_staff = models.BooleanField(('Стаф'), default=False)
    is_admin = models.BooleanField(('Админ'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    objects = UserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.fathers_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def lvl(self):
        return self.level

    @property
    def active(self):
        return self.is_active

    @property
    def firm(self):
        return self.firm_name
