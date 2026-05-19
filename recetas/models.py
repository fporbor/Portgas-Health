from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from usuarios.models import Like
from django.urls import reverse


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
        related_name="recetas_creadas"
    )

    objetivo = models.ForeignKey(
        Objetivo,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recetas"
    )

    alergia = models.ManyToManyField(
        Alergia,
        related_name="recetas"
    )

    descripcion = models.TextField(blank=True)
    likes = GenericRelation(Like)

    video = models.FileField(
        upload_to="recetas/",
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("recetas:detalle", args=[self.pk])

    def __str__(self):
        return self.nombre
