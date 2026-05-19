# gimnasios/urls.py
from django.urls import path
from .views import GimnasioListView, GimnasioDetailView, GimnasioCreateView, GimnasioUpdateView, GimnasioDeleteView


app_name = "gimnasios"

urlpatterns = [
    path("", GimnasioListView.as_view(), name="gym_lista"),
    path("<int:pk>/", GimnasioDetailView.as_view(), name="gym_detalle"),
    path("crear/", GimnasioCreateView.as_view(), name="gym_crear"),
    path("<int:pk>/editar/", GimnasioUpdateView.as_view(), name="gym_editar"),
    path("<int:pk>/eliminar/", GimnasioDeleteView.as_view(), name="gym_eliminar"),
]
