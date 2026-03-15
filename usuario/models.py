from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Usuario(AbstractUser):
    apellido2 = models.CharField(max_length=150, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    


class Like(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes"
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    contenido = GenericForeignKey("content_type", "object_id")

    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "content_type", "object_id")

    def __str__(self):
        return f"{self.usuario} dio like a {self.content_type} ({self.object_id})"

