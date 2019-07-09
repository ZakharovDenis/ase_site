from django.contrib import admin
from ase_site.data.models import Car, Company, Driver,GPS, GPSdata


class CarAdmin(admin.ModelAdmin):
    list_display=('cartype','label','max_weight','driver','gps')
    fieldsets=[
        (None,  {'fields':['cartype','label','max_weight','driver','gps']}),
    ]
    search_fields=('cartype','label','max_weight','driver','gps')

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','city','INN')
    search_fields=('name','city','INN')

class DriverAdmin(admin.ModelAdmin):
    list_display=('name','last_name','fathers_name','phone_number','org')
    fieldsets=[
        (None,  {'fields':['name','last_name','fathers_name','phone_number','org']}),
    ]
    search_fields=('name','last_name','fathers_name','phone_number','org')

class GPSAdmin(admin.ModelAdmin):
    list_display=('id',)
    add_fieldsets=[
        (None,{'fields':['id',]}),
    ]
    def has_change_permission(self,request,obj=None):
        return False

class WorkGroupAdmin(admin.ModelAdmin):
    fieldset=[
        (None,{'fields':['name','place','org']})
    ]
    filter_horizontal=('people',)

class GPSdataAdmin(admin.ModelAdmin):
    readonly_fields=('id','date','latitude','longitude')
    
    def has_add_permission(self,request,obj=None):
        return True

    def has_change_permission(self,request,obj=None):
        return False

    def has_delete_permission(self,request,obj=None):
        return False

admin.site.register(Car,CarAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Driver,DriverAdmin)
admin.site.register(GPS,GPSAdmin)
admin.site.register(GPSdata,GPSdataAdmin)