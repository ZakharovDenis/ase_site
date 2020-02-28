from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email', 'first_name', 'last_name', 'fathers_name',)
    list_filter = ('firm_name', 'level', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Линая информация', {'fields': ('first_name', 'last_name', 'fathers_name')}),
        ('Рабочая информация', {'fields': ('firm_name', 'level', 'phone',)}),
        ('Активация', {'fields': ('is_active',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email', 'first_name', 'last_name', 'fathers_name', ]
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
