from django.db import models
from django.contrib.auth.models import User

#modelo evento
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100, blank=True)
    privado = models.BooleanField(default=False)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)


    #relacion con asistentes
    asistentes = models.ManyToManyField(User, related_name='eventos_registrados')

    def __str__(self):
        return self.nombre