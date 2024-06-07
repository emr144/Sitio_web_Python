from django.db import models

# Create your models here.
class ClienteCla(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class EmpleadoCla(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    puesto = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.puesto}'

class ProveedorCla(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(max_length=100)
    rubro = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre