from ase_site.data.models import Car, Company, GPS, GPSdata, CarType
from django.contrib import admin


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'car_type', 'gps')
    fieldsets = [
        (None, {'fields': ['car_number', 'car_type', 'gps', 'connected_application']}),
    ]
    search_fields = ('car_number', 'car_type', 'gps', 'connected_application')


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('car_type',)
    fieldsets = [
        (None, {'fields': ['car_type', ]}),
    ]
    search_fields = ('car_type',)


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
    list_display = ('id_gps', 'date', 'latitude', 'longitude')

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Car, CarAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(GPS, GPSAdmin)
admin.site.register(GPSdata, GPSdataAdmin)
