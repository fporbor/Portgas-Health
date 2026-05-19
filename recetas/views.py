from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Receta, Alergia
from .forms import RecetaForm


# -----------------------------
# LISTA
# -----------------------------
class RecetaListView(ListView):
    model = Receta
    template_name = "recetas/rec_lista.html"
    context_object_name = "recetas"

    def get(self, request, *args, **kwargs):
        # Limpiar la sesión al volver a la lista
        request.session.pop('volver_a', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        recetas = (
            Receta.objects
            .select_related('objetivo', 'autor')
            .prefetch_related('alergia')
        )

        q = self.request.GET.get("q")
        if q:
            recetas = recetas.filter(nombre__icontains=q)

        objetivo = self.request.GET.get("objetivo")
        if objetivo:
            recetas = recetas.filter(objetivo__nombre__iexact=objetivo)

        alergias = self.request.GET.getlist("alergia")
        if alergias:
            recetas = recetas.exclude(alergia__nombre__in=alergias)

        cal_min = self.request.GET.get("cal_min")
        cal_max = self.request.GET.get("cal_max")
        if cal_min:
            recetas = recetas.filter(calorias__gte=int(cal_min))
        if cal_max:
            recetas = recetas.filter(calorias__lte=int(cal_max))

        pro_min = self.request.GET.get("pro_min")
        pro_max = self.request.GET.get("pro_max")
        if pro_min:
            recetas = recetas.filter(proteina__gte=int(pro_min))
        if pro_max:
            recetas = recetas.filter(proteina__lte=int(pro_max))

        orden = self.request.GET.get("orden")
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

        return recetas.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alergias"] = Alergia.objects.all()
        context["alergias_seleccionadas"] = self.request.GET.getlist("alergia")
        return context


# -----------------------------
# DETALLE
# -----------------------------
class RecetaDetailView(DetailView):
    model = Receta
    template_name = "recetas/rec_detalle.html"
    context_object_name = "receta"

    def get(self, request, *args, **kwargs):
        referer = request.META.get("HTTP_REFERER")

        # Guardar solo si vienes de una lista, no de editar/eliminar
        if referer and "editar" not in referer and "eliminar" not in referer:
            if "volver_a" not in request.session:
                request.session["volver_a"] = referer

        return super().get(request, *args, **kwargs)


# -----------------------------
# CREAR
# -----------------------------
class RecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetas/rec_crear.html"

    def form_valid(self, form):
        receta = form.save(commit=False)
        receta.autor = self.request.user
        receta.save()
        form.save_m2m()
        messages.success(self.request, "Receta creada correctamente.")
        return redirect("recetas:detalle", pk=receta.pk)


# -----------------------------
# EDITAR
# -----------------------------
class RecetaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = "recetas/rec_crear.html"

    def test_func(self):
        receta = self.get_object()
        return self.request.user.is_staff or self.request.user.is_superuser or receta.autor == self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Receta actualizada correctamente.")
        return redirect("recetas:detalle", pk=self.get_object().pk)


# -----------------------------
# ELIMINAR
# -----------------------------
class RecetaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receta
    template_name = "recetas/rec_eliminar.html"
    success_url = reverse_lazy("recetas:lista")

    def test_func(self):
        receta = self.get_object()
        return self.request.user.is_staff or self.request.user.is_superuser or receta.autor == self.request.user


    def delete(self, request, *args, **kwargs):
        messages.success(request, "Receta eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
