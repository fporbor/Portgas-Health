# gimnasios/urls.py
from django.urls import path
from .views import GimnasioListView, GimnasioDetailView


app_name = "gimnasio"

urlpatterns = [
    path("", GimnasioListView.as_view(), name="lista_gimnasios"),
    path("<int:pk>/", GimnasioDetailView.as_view(), name="detalle_gimnasio"),
]
