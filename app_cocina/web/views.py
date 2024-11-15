from django.shortcuts import render, get_object_or_404
from django.views import generic
from ingredientes.models import Categorias, Ingredientes, Dificultades, Recetas
from chartjs.views.lines import BaseLineChartView

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

def one_to_many(request, pk, format=None):
    one = Dificultades.objects.filter(id = pk).values()
    many = Recetas.objects.filter(recdif_fk = pk)
    return render(request, "web/one_to_many.html", {"one":one, "many":many})

def chart(request):
    labels = ['January', 'February', 'March', 'April',  'May',  'June', 'July'] 
    chartLabel = "my data"
    chartdata = [0, 10, 5, 2, 20, 30, 45] 
    data ={ 
            "labels":labels, 
            "chartLabel":chartLabel, 
            "chartdata":chartdata, 
             }
    return render(request, 'web/chart.html', {"mydata":data})

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 dataset to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='chart.html')
line_chart_json = LineChartJSONView.as_view()