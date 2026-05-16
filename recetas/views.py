from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Receta, Alergia
from .forms import RecetaForm

def lista_recetas(request):

    recetas = (
        Receta.objects
        .select_related('objetivo', 'autor')
        .prefetch_related('alergia')
    )

    # --- Search ---
    q = request.GET.get("q")
    if q:
        recetas = recetas.filter(nombre__icontains=q)

    # --- Objetivo ---
    objetivo = request.GET.get("objetivo")
    if objetivo:
        recetas = recetas.filter(objetivo__nombre__iexact=objetivo)

    # --- Alergias múltiples ---
    alergias_seleccionadas = request.GET.getlist("alergia")

    if alergias_seleccionadas:
        recetas = recetas.exclude(alergia__nombre__in=alergias_seleccionadas)

    # --- Calorías rango ---
    cal_min = request.GET.get("cal_min")
    cal_max = request.GET.get("cal_max")

    if cal_min:
        recetas = recetas.filter(calorias__gte=int(cal_min))

    if cal_max:
        recetas = recetas.filter(calorias__lte=int(cal_max))

    # --- Proteína rango ---
    pro_min = request.GET.get("pro_min")
    pro_max = request.GET.get("pro_max")

    if pro_min:
        recetas = recetas.filter(proteina__gte=int(pro_min))

    if pro_max:
        recetas = recetas.filter(proteina__lte=int(pro_max))

    # --- Ordenamiento ---
    orden = request.GET.get("orden")
    if orden == "nombre_asc":
        recetas = recetas.order_by("nombre")
    elif orden == "nombre_desc":
        recetas = recetas.order_by("-nombre")
    elif orden == "calorias_asc":
        recetas = recetas.order_by("calorias")
    elif orden == "calorias_desc":
        recetas = recetas.order_by("-calorias")
    elif orden == "proteina_asc":
        recetas = recetas.order_by("proteina")
    elif orden == "proteina_desc":
        recetas = recetas.order_by("-proteina")

    recetas = recetas.distinct()

    return render(request, 'recetas/rec_lista.html', {
        'recetas': recetas,
        'alergias': Alergia.objects.all(),
        'alergias_seleccionadas': alergias_seleccionadas,  # 👈 clave
    })

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
