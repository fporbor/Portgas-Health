from django.contrib import admin
from .models import Objetivo, Alergia, Receta


@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Alergia)
class AlergiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "autor",
        "objetivo",
        "proteina",
        "calorias",
        "total_likes",
    )
    search_fields = (
        "nombre",
        "autor__username",
        "objetivo__nombre",
        "alergia__nombre",
    )
    list_filter = ("objetivo", "alergia")
    filter_horizontal = ("alergia",)
    readonly_fields = ("total_likes",)

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = "Likes"
