from django.contrib import admin
from ase_site.data.models import Car, Company, GPS, GPSdata


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_type', 'gps')
    fieldsets=[
        (None,  {'fields': ['id', 'car_type', 'gps']}),
    ]
    search_fields = ('id', 'car_type', 'gps')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class GPSAdmin(admin.ModelAdmin):
    list_display = ('id',)
    add_fieldsets = [
        (None, {'fields': ['id', ]}),
    ]

    def has_change_permission(self, request, obj=None):
        return False


class GPSdataAdmin(admin.ModelAdmin):
    readonly_fields=('id', 'date', 'latitude', 'longitude')
    
    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Car, CarAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(GPS, GPSAdmin)
admin.site.register(GPSdata, GPSdataAdmin)
