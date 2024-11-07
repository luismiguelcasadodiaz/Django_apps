from django.shortcuts import render, get_object_or_404
from django.views import generic

from visualfact.models import Facturas, Detalles

# Create your views here.
class FacturasView(generic.ListView):
    template_name = "visualfact/facturas.html"
    context_object_name = "lista_facturas"

    def get_queryset(self):
        return Facturas.objects.all()
    
class FacturaDetalleView(generic.View):
    model = Facturas
    template_name = "visualfact/facturadetalle.html"

    def get(self, request, pk, format=None):
        myfactura = get_object_or_404(Facturas, id = pk)
        detalles =  Detalles.objects.filter(factura = pk)
        return render(request, self.template_name, {"factura":myfactura, "lista_detalles":detalles})