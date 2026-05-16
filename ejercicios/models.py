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

    video_url = models.URLField(blank=True, null=True)

    def youtube_id(self):
        from urllib.parse import urlparse, parse_qs

        if not self.video_url:
            return None

        url = urlparse(self.video_url)

        # watch?v=ID
        if url.hostname in ["www.youtube.com", "youtube.com"]:
            if url.path == "/watch":
                return parse_qs(url.query).get("v", [None])[0]

            # shorts/ID
            if url.path.startswith("/shorts/"):
                return url.path.split("/")[2]

        # youtu.be/ID
        if url.hostname == "youtu.be":
            return url.path[1:]

        return None



    def embed_url(self):
        """
        Devuelve la URL lista para incrustar en un iframe.
        """
        vid = self.youtube_id()
        if vid:
            return f"https://www.youtube.com/embed/{vid}"
        return None

    def get_absolute_url(self):
        return reverse("ejercicios:detalle", args=[self.pk])
    
    def __str__(self):
        return self.nombre
