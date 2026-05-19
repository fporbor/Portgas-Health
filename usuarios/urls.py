from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('<str:model>/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path("<int:pk>/", views.UsuarioDetalleView.as_view(), name="usuario_detalle"),
    path("<int:pk>/editar/", views.UsuarioEditarView.as_view(), name="usuario_editar"),
]
app_name = "usuarios"
