from django.views.generic import ListView, DetailView
from .models import Gimnasio, TipoGimnasio

class GimnasioListView(ListView):
    model = Gimnasio
    template_name = "gimnasios/gym_lista.html"
    context_object_name = "gimnasios"

    def get_queryset(self):
        queryset = super().get_queryset()

        provincia = self.request.GET.get("provincia")
        localidad = self.request.GET.get("localidad")
        nombre = self.request.GET.get("nombre")
        tipo = self.request.GET.get("tipo")
        orden = self.request.GET.get("orden")

        # --- Filtros ---
        if provincia:
            queryset = queryset.filter(provincia__icontains=provincia)

        if localidad:
            queryset = queryset.filter(localidad__icontains=localidad)

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        if tipo:
            queryset = queryset.filter(tipo_gimnasio__id=tipo)

        # --- Orden ---
        if orden == "nombre_asc":
            queryset = queryset.order_by("nombre")
        elif orden == "nombre_desc":
            queryset = queryset.order_by("-nombre")
        elif orden == "provincia_asc":
            queryset = queryset.order_by("provincia")
        elif orden == "provincia_desc":
            queryset = queryset.order_by("-provincia")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos"] = TipoGimnasio.objects.all()
        return context


class GimnasioDetailView(DetailView):
    model = Gimnasio
    template_name = "gimnasios/gym_detalle.html"
    context_object_name = "gimnasio"
