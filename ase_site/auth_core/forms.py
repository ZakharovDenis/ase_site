from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .choices import *
from .models import User


class UserLoginForm(forms.Form):
    Login = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'textbox'}))
    Password = forms.CharField(label='',
                               widget=(forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'textbox'})))


class UserForm(forms.ModelForm):
    # username=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Логин','class':'textbox'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'textbox'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'textbox'}))
    fathers_name = forms.CharField(required=False, label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'textbox'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'textbox'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'textbox'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Подтвердите пароль', 'class': 'textbox'}))
    firm_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Название фирмы', 'class': 'textbox'}))
    level = forms.ChoiceField(label='', choices=STATUS_CHOICES,
                              widget=forms.Select(attrs={'placeholder': 'Статус сотрудника', 'class': 'textbox'}))
    phone = cellphone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': (u'Cellphone'), 'class': "form-control"}),
        label=(u'Cellphone number'),
        required=False,
        initial='+7'
    )

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'fathers_name', 'email', 'firm_name', 'level', 'password', 'phone')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Адрес электронной почты используется")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        return confirm_password

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'is_active')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
        'email', 'password', 'first_name', 'last_name', 'fathers_name', 'email', 'firm_name', 'level', 'is_active',
        'phone')

    def clean_password(self):
        return self.initial["password"]
