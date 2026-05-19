from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from usuarios.models import Like
from django.urls import reverse


class TipoEjercicio(models.Model):  # hipertrofia, fuerza, resistencia, etc.
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class GrupoMuscular(models.Model):  # pecho, espalda, piernas, etc.
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ejercicios_creados"
    )

    tipo_ejercicio = models.ForeignKey(
        TipoEjercicio,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ejercicios"
    )

    grupo_muscular = models.ManyToManyField(
        GrupoMuscular,
        related_name="ejercicios"
    )

    descripcion = models.TextField(blank=True)
    likes = GenericRelation(Like)

    video = models.FileField(
        upload_to="ejercicios/",
        blank=True,
        null=True,
        default="ejercicios/ejemplo.mp4"
    )

    def get_absolute_url(self):
        return reverse("ejercicios:detalle", args=[self.pk])

    def __str__(self):
        return self.nombre

