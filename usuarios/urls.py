from django.urls import path
from . import views

urlpatterns = [
    path('<str:model>/<int:pk>/like/', views.toggle_like, name='toggle_like'),
]
app_name = "usuarios"
