
from django.contrib import admin
from .models import ClienteCla, EmpleadoCla, ProveedorCla


# Register your models here.
admin.site.register(ClienteCla)
admin.site.register(EmpleadoCla)
admin.site.register(ProveedorCla)