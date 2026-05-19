from django.urls import path
from .views import (
    EjercicioListView,
    EjercicioDetailView,
    EjercicioCreateView,
    EjercicioUpdateView,
    EjercicioDeleteView,
)

app_name = 'ejercicios'

urlpatterns = [
    path('', EjercicioListView.as_view(), name='lista'),
    path('<int:pk>/', EjercicioDetailView.as_view(), name='detalle'),
    path('crear/', EjercicioCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', EjercicioUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', EjercicioDeleteView.as_view(), name='eliminar'),
]
