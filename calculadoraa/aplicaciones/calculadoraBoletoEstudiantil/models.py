from django.db import models


class Estudiante(models.Model):
    id = models.AutoField(primary_key = True)
    cantidad_bondis = models.PositiveIntegerField(default = 0, null = True)
    cantidad_subtes = models.PositiveIntegerField(default = 0, null = True)
    cantidad_trenes = models.PositiveIntegerField(default = 0, null = True)

    cantidad_dias = models.PositiveIntegerField(default = 0, null=True)
    costo_mensual = models.IntegerField(default = 0)
    costo_mensual_diciembre = models.IntegerField(default= 0)
    
# Create your models here.
