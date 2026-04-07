from django.urls import path
from . import views

app_name = 'ejercicios'

urlpatterns = [
    path('', views.lista_ejercicios, name='lista'),
    path('<int:pk>/', views.detalle_ejercicio, name='detalle'),
    path('crear/', views.crear_ejercicio, name='crear'),
    path('<int:pk>/editar/', views.editar_ejercicio, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_ejercicio, name='eliminar'),
]