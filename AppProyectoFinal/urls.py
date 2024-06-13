from django.urls import path
from AppProyectoFinal.views import inicio,cliente, empleado, proveedor
from AppProyectoFinal.views import ClienteList, ClienteDetail, ClienteCreate, ClienteUpdate ,ClienteDelete
from AppProyectoFinal.views import EmpleadoList, EmpleadoDetail, EmpleadoCreate, EmpleadoUpdate ,EmpleadoDelete
from AppProyectoFinal.views import ProveedorList, ProveedorDetail, ProveedorCreate, ProveedorUpdate ,ProveedorDelete
from AppProyectoFinal.views import buscar, ingresar




urlpatterns = [
    
    path('inicio/', inicio,name="inicio"),
    path('cliente/', cliente,name="cliente"),
    path('empleado/', empleado,name="empleado"),
    path('proveedor/', proveedor,name="proveedor"),
    path('ingresar/', ingresar,name="ingresar"),

    path('buscar/', buscar, name='buscar'),

    path('cliente-lista/', ClienteList.as_view(), name='ListaCliente'),
    path('cliente-detalle/<pk>/', ClienteDetail.as_view(), name='DetalleCliente'),
    path('cliente-crea/', ClienteCreate.as_view(), name='CreaCliente'),
    path('cliente-actualiza/<pk>/', ClienteUpdate.as_view(), name='ActualizaCliente'),
    path('cliente-elimina/<pk>/', ClienteDelete.as_view(), name='EliminaCliente'),

    path('empleado_lista/', EmpleadoList.as_view(), name='ListaEmpleado'),
    path('empleado-detalle/<pk>/', EmpleadoDetail.as_view(), name='DetalleEmpleado'),
    path('empleado-crea/', EmpleadoCreate.as_view(), name='CreaEmpleado'),
    path('empleado-actualiza/<pk>/', EmpleadoUpdate.as_view(), name='ActualizaEmpleado'),
    path('empleado-elimina/<pk>/', EmpleadoDelete.as_view(), name='EliminaEmpleado'),

    path('proveedor_lista/', ProveedorList.as_view(), name='ListaProveedor'),
    path('proveedor-detalle/<pk>/', ProveedorDetail.as_view(), name='DetalleProveedor'),
    path('proveedor-crea/', ProveedorCreate.as_view(), name='CreaProveedor'),
    path('proveedor-actualiza/<pk>/', ProveedorUpdate.as_view(), name='ActualizaProveedor'),
    path('proveedor-elimina/<pk>/', ProveedorDelete.as_view(), name='EliminaProveedor'),

       ]