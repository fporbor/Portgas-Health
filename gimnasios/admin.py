from django.contrib import admin
from .models import TipoGimnasio, Gimnasio


@admin.register(TipoGimnasio)
class TipoGimnasioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Gimnasio)
class GimnasioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "provincia",
        "localidad",
        "tipo_gimnasio",
        "total_likes",
        "foto"
    )
    list_filter = ("provincia", "localidad", "tipo_gimnasio")
    search_fields = ("nombre", "provincia", "localidad", "email")
    readonly_fields = ("total_likes",)

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = "Likes"
