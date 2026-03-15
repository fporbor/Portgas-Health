from django.db import models
from django.conf import settings


class Objetivo(models.Model):  
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Alergia(models.Model): 
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    proteina = models.IntegerField()
    calorias = models.IntegerField()

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="autor"
    )

    objetivo = models.ForeignKey(
        Objetivo,
        on_delete=models.SET_NULL,
        null=True,
        related_name="objetivo"
    )

    alergia = models.ManyToManyField(
        Alergia,
        related_name="alergia"
    )

    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre