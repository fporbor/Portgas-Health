from django.urls import path
from .views import (
    RecetaListView,
    RecetaDetailView,
    RecetaCreateView,
    RecetaUpdateView,
    RecetaDeleteView,
)

app_name = 'recetas'

urlpatterns = [
    path('', RecetaListView.as_view(), name='lista'),
    path('<int:pk>/', RecetaDetailView.as_view(), name='detalle'),
    path('crear/', RecetaCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', RecetaUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', RecetaDeleteView.as_view(), name='eliminar'),
]
