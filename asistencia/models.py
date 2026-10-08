from django.db import models

# Create your models here.

class Asistencia(models.Model):

    tipo_documento = models.CharField(max_length=20)
    documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre