from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from usuarios.models import Like
from django.urls import reverse


class TipoGimnasio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    provincia = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    url = models.URLField()

    tipo_gimnasio = models.ForeignKey(
        TipoGimnasio,
        on_delete=models.SET_NULL,
        null=True,
        related_name="gimnasios"
    )

    likes = GenericRelation(Like)

    foto = models.URLField(
    blank=True,
    null=True
    )


    def get_absolute_url(self):
        return reverse("gimnasios:gym_detalle", args=[self.pk])

    def __str__(self):
        return f"{self.nombre} - {self.localidad} ({self.provincia})"

