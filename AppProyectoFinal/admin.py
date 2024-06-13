
from django.contrib import admin
from .models import ClienteCla, EmpleadoCla, ProveedorCla
from .form import ClienteForm, EmpleadoForm, ProveedorForm 

class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm

class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoForm

class ProveedorAdmin(admin.ModelAdmin):
    form = ProveedorForm


# Register your models here.
admin.site.register(ClienteCla, ClienteAdmin)
admin.site.register(EmpleadoCla, EmpleadoAdmin)
admin.site.register(ProveedorCla, ProveedorAdmin)