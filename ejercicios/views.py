from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ejercicio
from .forms import EjercicioForm


def lista_ejercicios(request):
    ejercicios = Ejercicio.objects.select_related('tipo_ejercicio', 'autor') \
                                  .prefetch_related('grupo_muscular').all()
    return render(request, 'ejercicios/ejec_lista.html', {'ejercicios': ejercicios})


def detalle_ejercicio(request, pk):
    ejercicio = get_object_or_404(
        Ejercicio.objects.select_related('tipo_ejercicio', 'autor')
                         .prefetch_related('grupo_muscular'),
        pk=pk
    )
    return render(request, 'ejercicios/ejec_detalle.html', {'ejercicio': ejercicio})


@login_required
def crear_ejercicio(request):
    if request.method == 'POST':
        form = EjercicioForm(request.POST)
        if form.is_valid():
            ejercicio = form.save(commit=False)
            ejercicio.autor = request.user
            ejercicio.save()
            form.save_m2m()  # Necesario para guardar ManyToMany (grupo_muscular)
            messages.success(request, 'Ejercicio creado correctamente.')
            return redirect('ejercicios:detalle', pk=ejercicio.pk)
    else:
        form = EjercicioForm()
    return render(request, 'ejercicios/ejec_crear.html', {'form': form, 'accion': 'Crear'})


@login_required
def editar_ejercicio(request, pk):
    ejercicio = get_object_or_404(Ejercicio, pk=pk)

    if ejercicio.autor != request.user:
        messages.error(request, 'No tienes permiso para editar este ejercicio.')
        return redirect('ejercicios:detalle', pk=pk)

    if request.method == 'POST':
        form = EjercicioForm(request.POST, instance=ejercicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ejercicio actualizado correctamente.')
            return redirect('ejercicios:detalle', pk=ejercicio.pk)
    else:
        form = EjercicioForm(instance=ejercicio)
    return render(request, 'ejercicios/ejec_crear.html', {'form': form, 'accion': 'Editar', 'ejercicio': ejercicio})


@login_required
def eliminar_ejercicio(request, pk):
    ejercicio = get_object_or_404(Ejercicio, pk=pk)

    if ejercicio.autor != request.user:
        messages.error(request, 'No tienes permiso para eliminar este ejercicio.')
        return redirect('ejercicios:detalle', pk=pk)

    if request.method == 'POST':
        ejercicio.delete()
        messages.success(request, 'Ejercicio eliminado correctamente.')
        return redirect('ejercicios:lista')
    return render(request, 'ejercicios/ejec_crear.html', {'ejercicio': ejercicio})