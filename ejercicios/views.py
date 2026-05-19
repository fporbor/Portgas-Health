from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Ejercicio
from .forms import EjercicioForm


# -----------------------------
# LISTA
# -----------------------------
class EjercicioListView(ListView):
    model = Ejercicio
    template_name = "ejercicios/ejec_lista.html"
    context_object_name = "ejercicios"

    def get(self, request, *args, **kwargs):
        # Limpiar la sesión al volver a la lista
        request.session.pop('volver_a', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        ejercicios = (
            Ejercicio.objects
            .select_related('tipo_ejercicio', 'autor')
            .prefetch_related('grupo_muscular')
        )

        q = self.request.GET.get("q")
        tipo = self.request.GET.get("tipo")
        grupo = self.request.GET.get("grupo")

        if q:
            ejercicios = ejercicios.filter(nombre__icontains=q)

        if tipo:
            ejercicios = ejercicios.filter(tipo_ejercicio__nombre=tipo)

        if grupo:
            ejercicios = ejercicios.filter(grupo_muscular__nombre=grupo)

        orden = self.request.GET.get("orden")
        if orden == "nombre_asc":
            ejercicios = ejercicios.order_by("nombre")
        elif orden == "nombre_desc":
            ejercicios = ejercicios.order_by("-nombre")
        elif orden == "tipo_asc":
            ejercicios = ejercicios.order_by("tipo_ejercicio__nombre")
        elif orden == "tipo_desc":
            ejercicios = ejercicios.order_by("-tipo_ejercicio__nombre")
        elif orden == "grupo_asc":
            ejercicios = ejercicios.order_by("grupo_muscular__nombre")
        elif orden == "grupo_desc":
            ejercicios = ejercicios.order_by("-grupo_muscular__nombre")

        return ejercicios


# -----------------------------
# DETALLE
# -----------------------------
class EjercicioDetailView(DetailView):
    model = Ejercicio
    template_name = "ejercicios/ejec_detalle.html"
    context_object_name = "ejercicio"

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
class EjercicioCreateView(LoginRequiredMixin, CreateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = "ejercicios/ejec_crear.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accion"] = "Crear"
        context["ejercicio"] = None
        return context

    def form_valid(self, form):
        ejercicio = form.save(commit=False)
        ejercicio.autor = self.request.user
        ejercicio.save()
        form.save_m2m()
        messages.success(self.request, "Ejercicio creado correctamente.")
        return redirect("ejercicios:detalle", pk=ejercicio.pk)


# -----------------------------
# EDITAR
# -----------------------------
class EjercicioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = "ejercicios/ejec_crear.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accion"] = "Editar"
        context["ejercicio"] = self.get_object()
        return context

    def test_func(self):
        ejercicio = self.get_object()
        user = self.request.user

        # Autor, admin o superusuario
        return (
            ejercicio.autor is None or
            ejercicio.autor == user or
            user.is_staff or
            user.is_superuser
        )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ejercicio actualizado correctamente.")
        return redirect("ejercicios:detalle", pk=self.get_object().pk)


# -----------------------------
# ELIMINAR
# -----------------------------
class EjercicioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ejercicio
    template_name = "ejercicios/ejec_eliminar.html"
    success_url = reverse_lazy("ejercicios:lista")

    def test_func(self):
        ejercicio = self.get_object()
        user = self.request.user

        return (
            ejercicio.autor is None or
            ejercicio.autor == user or
            user.is_staff or
            user.is_superuser
        )

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Ejercicio eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


