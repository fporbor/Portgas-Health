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
        return reverse("gimnasios:detalle_gimnasio", args=[self.pk])
    
    def __str__(self):
        return f"{self.nombre} - {self.localidad} ({self.provincia})"
