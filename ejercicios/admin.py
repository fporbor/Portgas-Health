from django.contrib import admin
from .models import TipoEjercicio, GrupoMuscular, Ejercicio


@admin.register(TipoEjercicio)
class TipoEjercicioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(GrupoMuscular)
class GrupoMuscularAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "autor",
        "tipo_ejercicio",
        "total_likes",
    )
    search_fields = ("nombre", "autor__username", "tipo_ejercicio__nombre")
    list_filter = ("tipo_ejercicio", "grupo_muscular")
    filter_horizontal = ("grupo_muscular",)
    readonly_fields = ("total_likes",)

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = "Likes"

