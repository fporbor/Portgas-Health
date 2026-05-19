from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gimnasio, TipoGimnasio
from .forms import GimnasioForm


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

        if provincia:
            queryset = queryset.filter(provincia__icontains=provincia)

        if localidad:
            queryset = queryset.filter(localidad__icontains=localidad)

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        if tipo:
            queryset = queryset.filter(tipo_gimnasio__id=tipo)

        if orden == "nombre_asc":
            queryset = queryset.order_by("nombre")
        elif orden == "nombre_desc":
            queryset = queryset.order_by("-nombre")
        elif orden == "provincia_asc":
            queryset = queryset.order_by("provincia")
        elif orden == "provincia_desc":
            queryset = queryset.order_by("-provincia")

        return queryset
    
    def get(self, request, *args, **kwargs):
        request.session.pop('volver_a', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos"] = TipoGimnasio.objects.all()
        return context


class GimnasioDetailView(DetailView):
    model = Gimnasio
    template_name = "gimnasios/gym_detalle.html"
    context_object_name = "gimnasio"

    def get(self, request, *args, **kwargs):
        if 'volver_a' not in request.session:
            request.session['volver_a'] = request.META.get('HTTP_REFERER')
        return super().get(request, *args, **kwargs)

class GimnasioCreateView(CreateView):
    model = Gimnasio
    form_class = GimnasioForm
    template_name = "gimnasios/gym_crear.html"

    def get_success_url(self):
        return reverse_lazy("gimnasios:gym_detalle", args=[self.object.pk])


class GimnasioUpdateView(UpdateView):
    model = Gimnasio
    form_class = GimnasioForm
    template_name = "gimnasios/gym_editar.html"

    def get_success_url(self):
        return reverse_lazy("gimnasios:gym_detalle", args=[self.object.pk])


class GimnasioDeleteView(DeleteView):
    model = Gimnasio
    template_name = "gimnasios/gym_eliminar.html"
    success_url = reverse_lazy("gimnasios:gym_lista")
