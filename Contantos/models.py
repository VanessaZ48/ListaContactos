from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=100)
    Gmail = models.EmailField(max_length=50)
    Fecha_Nacimiento = models.DateField(null=True, blank=True)
    Telefono = models.CharField(max_length=15, null=True, blank=True)
    Fecha_Creacion = models.DateField(auto_now_add=True)
