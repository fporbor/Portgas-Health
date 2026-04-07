from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Receta
from .forms import RecetaForm


def lista_recetas(request):
    recetas = Receta.objects.select_related('objetivo', 'autor') \
                            .prefetch_related('alergia').all()
    return render(request, 'recetas/rec_lista.html', {'recetas': recetas})


def detalle_receta(request, pk):
    receta = get_object_or_404(
        Receta.objects.select_related('objetivo', 'autor')
                      .prefetch_related('alergia'),
        pk=pk
    )
    return render(request, 'recetas/rec_detalle.html', {'receta': receta})


@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            form.save_m2m()  # Necesario para guardar ManyToMany (alergia)
            messages.success(request, 'Receta creada correctamente.')
            return redirect('recetas:detalle', pk=receta.pk)
    else:
        form = RecetaForm()
    return render(request, 'recetas/rec_crear.html', {'form': form, 'accion': 'Crear'})


@login_required
def editar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)

    if receta.autor != request.user:
        messages.error(request, 'No tienes permiso para editar esta receta.')
        return redirect('recetas:detalle', pk=pk)

    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta actualizada correctamente.')
            return redirect('recetas:detalle', pk=receta.pk)
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'recetas/rec_crear.html', {'form': form, 'accion': 'Editar', 'receta': receta})


@login_required
def eliminar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)

    if receta.autor != request.user:
        messages.error(request, 'No tienes permiso para eliminar esta receta.')
        return redirect('recetas:detalle', pk=pk)

    if request.method == 'POST':
        receta.delete()
        messages.success(request, 'Receta eliminada correctamente.')
        return redirect('recetas:lista')
    return render(request, 'recetas/rec_eliminar.html', {'receta': receta})