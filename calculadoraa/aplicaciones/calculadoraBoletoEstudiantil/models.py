from django.db import models


class Estudiante(models.Model):
    id = models.AutoField(primary_key = True)
    cantidadBondis = models.CharField(max_length = 100)
    cantidadSubtes = models.CharField(max_length = 100)
    cantidadTrenes = models.CharField(max_length = 100)
# Create your models here.
