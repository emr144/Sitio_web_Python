from django.contrib import admin
from django import forms
from .models import ProveedorCla, ClienteCla, EmpleadoCla


class ClienteForm(forms.ModelForm):
     class Meta:
          model=ClienteCla
          fields=["nombre","apellido","email","telefono","direccion"]


class EmpleadoForm(forms.ModelForm):
     class Meta:
          model=EmpleadoCla
          fields=["nombre","apellido","email","telefono","puesto"]

class ProveedorForm(forms.ModelForm):
     class Meta:
          model=ProveedorCla
          fields=["nombre","email","telefono","rubro","direccion"]

class Buscar(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
    category = forms.ChoiceField(choices=[
        ('clientes', 'Clientes'),
        ('empleados', 'Empleados'),
        ('proveedores', 'Proveedores')
    ])
    
    