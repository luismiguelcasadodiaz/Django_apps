from django.shortcuts import render, get_object_or_404
from django.views import generic
from ingredientes.models import Categorias

# Create your views here.
class CategoriasView(generic.ListView):
    template_name = "web/categorias.html"
    context_object_name = "lista_categorias"

    def get_queryset(self):
        return Categorias.objects.all()
    
class CategoriasDetalleView(generic.DateDetailView):
    model = Categorias
    template_name = "web/categoriadetalle.html"

    def get(self, request, pk, format=None):
        categoria = get_object_or_404(Categorias, id = pk)
        return render(request, "web/categoriadetalle.html", {"categoria":categoria})
