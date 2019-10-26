from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin


class UserAdmin(BaseUserAdmin):
    form=UserAdminChangeForm
    add_form=UserAdminCreationForm
    #class Meta:
    #    model=User
    list_display=('email','first_name','last_name','fathers_name', )
    #list_display=('email','is_admin')
    list_filter=('firm_name','level','is_active',)
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Линая информация', {'fields': ('first_name', 'last_name', 'fathers_name')}),
        ('Рабочая информация', {'fields': ('firm_name', 'level',)}),
        ('Активация', {'fields':('is_active',)})
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2')}
        ),
    )
    search_fields=['email','first_name','last_name','fathers_name',]
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
