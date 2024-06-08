from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppProyectoFinal/', include("AppProyectoFinal.urls")),
    path("",include("AppProyectoFinal.urls")),

    path('admin/', admin.site.urls),
    path('', include('Startapp.urls')),  # Asegúrate de reemplazar 'Startapp' con el nombre de tu aplicación
]