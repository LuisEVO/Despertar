from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Marcacion(models.Model):
    fecha = models.DateField(blank=True)
    hora = models.TimeField(blank=True)
    usuario = models.ForeignKey(User)

    class Meta:
        ordering = ['usuario']

    def __str__(self):
        return '%s' % self.usuario