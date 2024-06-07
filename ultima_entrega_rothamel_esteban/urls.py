from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppProyectoFinal/', include("AppProyectoFinal.urls")),
    path("",include("AppProyectoFinal.urls")),
    
]
