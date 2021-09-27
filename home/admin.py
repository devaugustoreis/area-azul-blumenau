from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone1', 'email', 'credits', 'address']
    list_display_links = ['id', 'name']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'license_plate', 'timer', 'vehicle_type']
    list_display_links = ['id', 'license_plate']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'zip_code', 'state', 'city', 'district', 'street_name', 'house_number']

admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Address, AddressAdmin)