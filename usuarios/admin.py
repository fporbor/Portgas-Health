from django.contrib import admin
from .models import Usuario, Like


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "apellido2",
        "email",
        "telefono",
        "fecha_nacimiento",
        "is_staff",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "apellido2",
        "email",
        "telefono",
    )
    list_filter = ("is_staff", "is_superuser", "is_active")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "content_type",
        "object_id",
        "fecha",
        "objeto",
    )
    search_fields = (
        "usuario__username",
        "content_type__model",
        "object_id",
    )
    list_filter = ("content_type", "fecha")
    readonly_fields = ("fecha",)

    def objeto(self, obj):
        return str(obj.content_object)
    objeto.short_description = "Objeto liked"
