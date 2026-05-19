from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from .models import Like
from ejercicios.models import Ejercicio
from recetas.models import Receta
from gimnasios.models import Gimnasio
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UsuarioEditarForm
from .forms import LoginForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def toggle_like(request, model, pk):
    modelos = {
        "ejercicio": Ejercicio,
        "receta": Receta,
        "gimnasio": Gimnasio,
    }

    if model not in modelos:
        return redirect("/")

    ModelClass = modelos[model]
    obj = get_object_or_404(ModelClass, pk=pk)

    content_type = ContentType.objects.get_for_model(ModelClass)

    like, created = Like.objects.get_or_create(
        usuario=request.user,
        content_type=content_type,
        object_id=obj.id
    )

    if not created:
        like.delete()

    return redirect(obj.get_absolute_url())

User = get_user_model()

class UsuarioDetalleView(DetailView):
    model = User
    template_name = "usuarios/usuario_detalle.html"
    context_object_name = "usuario"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.get_object()

        likes = usuario.likes.select_related("content_type")

        context["likes"] = likes
        context["likes_gimnasios"] = likes.filter(content_type__model="gimnasio")
        context["likes_ejercicios"] = likes.filter(content_type__model="ejercicio")
        context["likes_recetas"] = likes.filter(content_type__model="receta")

        return context

class UsuarioEditarView(UpdateView):
    model = User
    form_class = UsuarioEditarForm
    template_name = "usuarios/usuario_editar.html"

    def get_success_url(self):
        return reverse_lazy("usuarios:usuario_detalle", args=[self.object.pk])

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs["pk"]:
            return redirect("usuarios:usuario_detalle", pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)
