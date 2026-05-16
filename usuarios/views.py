from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

from .models import Like
from ejercicios.models import Ejercicio
from recetas.models import Receta
from gimnasios.models import Gimnasio

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