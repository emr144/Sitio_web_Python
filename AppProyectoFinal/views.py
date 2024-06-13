from django.urls import reverse_lazy
from django.shortcuts import render
from .models import ClienteCla, EmpleadoCla, ProveedorCla
from .form import Buscar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(req):
     form = Buscar() 
     return render  (req,"Inicio.html",{'form': form})

def cliente(req):
     cliente=ClienteCla.objects.all()
     return render  (req,"Clientes.html",{"clientes":cliente})

def empleado(req):
     empleado=EmpleadoCla.objects.all()
     return render  (req,"Empleados.html",{"empleado":empleado})

def proveedor(req):
     proveedor=ProveedorCla.objects.all()
     return render  (req,"Proveedores.html",{"proveedor":proveedor})

def ingresar(req):
     return render  (req,"Ingresa.html")


#Buscador de personas segun su categoria



def buscar(request):
    form = Buscar(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        category = form.cleaned_data['category']
        if category == 'clientes':
            results = ClienteCla.objects.filter(nombre__icontains=query)
        elif category == 'empleados':
            results = EmpleadoCla.objects.filter(nombre__icontains=query)
        elif category == 'proveedores':
            results = ProveedorCla.objects.filter(nombre__icontains=query)
    return render(request, 'formularioBusqueda.html', {'form': form, 'results': results})


#Clases para las distintas pestañas

#Clientes

class ClienteList(LoginRequiredMixin,ListView):
    model = ClienteCla
    template_name = "Cliente_list.html"
    context_object_name="clientes"

class ClienteDetail(DetailView):
    model = ClienteCla
    template_name = "Cliente_detail.html"
    context_object_name="clientes"

class ClienteCreate(CreateView):
    model=ClienteCla
    template_name="Cliente_create.html"
    fields=["nombre","apellido","telefono","direccion","email"]
    success_url=reverse_lazy('ListaCliente')

class ClienteUpdate(UpdateView):
    model=ClienteCla
    template_name="Cliente_update.html"
    fields=("__all__")
    success_url=reverse_lazy('ListaCliente')
    context_object_name="clientes"

class ClienteDelete(DeleteView):
    model=ClienteCla
    template_name="Cliente_delete.html"
    success_url=reverse_lazy('ListaCliente')
    
#Empleado
class EmpleadoList(LoginRequiredMixin, ListView):
    model = EmpleadoCla
    template_name = "Empleado_list.html"
    context_object_name="empleados"

class EmpleadoDetail(DetailView):
    model = EmpleadoCla
    template_name = "Empleado_detail.html"
    context_object_name="empleado"

class EmpleadoCreate(CreateView):
    model=EmpleadoCla
    template_name="Empleado_create.html"
    fields=["nombre","apellido","telefono","puesto","email"]
    success_url=reverse_lazy('ListaEmpleado')

class EmpleadoUpdate(UpdateView):
    model=EmpleadoCla
    template_name="Empleado_update.html"
    fields=("__all__")
    success_url=reverse_lazy('ListaEmpleado')
    context_object_name="empleados"

class EmpleadoDelete(DeleteView):
    model=EmpleadoCla
    template_name="Empleado_delete.html"
    success_url=reverse_lazy('ListaEmpleado')

#Proveedor
class ProveedorList(LoginRequiredMixin, ListView):
    model = ProveedorCla
    template_name = "Proveedor_list.html"
    context_object_name="proveedores"

class ProveedorDetail(DetailView):
    model = ProveedorCla
    template_name = "Proveedor_detail.html"
    context_object_name="proveedor"

class ProveedorCreate(CreateView):
    model=ProveedorCla
    template_name="Proveedor_create.html"
    fields=["nombre","rubro","telefono","direccion","email"]
    success_url=reverse_lazy('ListaProveedor')

class ProveedorUpdate(UpdateView):
    model=ProveedorCla
    template_name="Proveedor_update.html"
    fields=("__all__")
    success_url=reverse_lazy('ListaProveedor')
    context_object_name="proveedores"

class ProveedorDelete(DeleteView):
    model=ProveedorCla
    template_name="Proveedor_delete.html"
    success_url=reverse_lazy('ListaProveedor')

