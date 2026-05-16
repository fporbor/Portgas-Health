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
        return reverse("recetas:detalle", args=[self.pk])

    def __str__(self):
        return self.nombre