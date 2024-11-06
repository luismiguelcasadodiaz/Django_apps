from django.shortcuts import render, get_object_or_404
from django.views import generic
from ingredientes.models import Categorias, Ingredientes

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
    

def testcat(request):
    lista_cat = Categorias.objects.all().values()
    new_lista_cat = []
    for dato in lista_cat:
        new_lista_cat.append({'id':dato['id'], 'datogenerico':dato['catnom']})
    
    return render(request, "web/test.html", {"lista_datos":new_lista_cat})

def testing(request):
    lista_cat = Ingredientes.objects.all().values()
    new_lista_cat = []
    for dato in lista_cat:
        new_lista_cat.append({'id':dato['id'], 'datogenerico':dato['ingnom']})
    
    return render(request, "web/test.html", {"lista_datos":new_lista_cat})
