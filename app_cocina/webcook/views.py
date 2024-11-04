
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
from ingredientes.models import Ingredientes, Temporadas, Dificultades, Categorias, Recetas, IngredientesRecetas
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class DificultadesView(generic.ListView):
    template_name = "webcook/dificultades.html"
    context_object_name = "lista_dificultades"

    def get_queryset(self):
        return Dificultades.objects.all()

class DificultadesDetalleView(generic.DetailView):
    model = Temporadas
    template_name = "webcook/dificultaddetalle.html"

    def get_object(self, pk):
        try:
            return Dificultades.objects.get(pk=pk)
        except Dificultades.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        dificultad = get_object_or_404(Dificultades, id = pk)
        return render(request, "webcook/dificultaddetalle.html", {"dificultad":dificultad})

class CategoriasView(generic.ListView):
    template_name = "webcook/categorias.html"
    context_object_name = "lista_categorias"

    def get_queryset(self):
        return Categorias.objects.all()
    
class CategoriasDetalleView(generic.DateDetailView):
    model = Categorias
    template_name = "webcook/categoriasdetalle.html"

    def get(self, request, pk, format=None):
        categoria = get_object_or_404(Categorias, id = pk)
        return render(request, "webcook/categoriadetalle.html", {"categoria":categoria})

class TemporadasView(generic.ListView):
    template_name = "webcook/temporadas.html"
    context_object_name = "lista_temporadas"

    def queryset(self):
        return Temporadas.objects.all()
    
class TemporadasDetalleView(generic.DetailView):
    model = Temporadas
    template_name = "webcook/temporadadetalle.html"

    def get(self, request, pk, format=None):
        temporada = get_object_or_404(Temporadas, id = pk)
        return render(request, "webcook/temporadadetalle.html", {"temporada":temporada})

class IngredientesView(generic.ListView):
    template_name = "webcook/ingredientes.html"
    context_object_name = "lista_ingredientes"
    
    def get_queryset(self):
        return Ingredientes.objects.order_by('ingnom')
             
class IngredientesDetalleView(generic.View):

    def get(self, request, pk, format=None):
        ingrediente = get_object_or_404(Ingredientes, id = pk)
        print(f"el tipo de ingredientees {type(ingrediente)}\n")
        print(f"nom = {ingrediente.ingnom}, temp={ingrediente.ingtemp_fk}")
        return render(request, "webcook/ingredientedetalle.html", {"ingrediente":ingrediente})

    def put(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        serializer = IngredientesSerializers(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
    
class RecetasView(generic.ListView):
    template_name = "webcook/recetas.html"
    context_object_name = "lista_recetas"
    
    def get_queryset(self):
        return Recetas.objects.order_by('rectem')

class RecetasDetalleView(generic.View):

    def get(self, request, pk, format=None):
        receta = get_object_or_404(Recetas, id = pk) 
        return render(request, "webcook/recetadetalle.html", {"receta":receta})
    
    def put(self, request, pk, format=None):
        receta = self.get_object(pk)
        serializer = RecetasSerializers(receta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        receta = self.get_object(pk)
        receta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IngredientesRecetas_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        ingredientesrecetas = IngredientesRecetas.objects.all()
        serializer = IngredientesRecetasSerializers(ingredientesrecetas, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        if isinstance(request.data, list):
            serializer = IngredientesRecetasSerializers(data=request.data, many=True)
        else:
            serializer = IngredientesRecetasSerializers(data=request.data, many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientesRecetas_APIView_Detail(APIView):

    def get_object(self, ingrecrec_fk):
        try:
            return IngredientesRecetas.objects.get(ingrecrec_fk=ingrecrec_fk)
        except IngredientesRecetas.DoesNotExist:
            raise Http404
    def get(self, request, receta_bruta, format=None):
        receta = ' '.split(receta_bruta, '%20')
        try:
            cod_receta = Recetas.objects.filter(recnom=receta)
            print(f"datos {receta} del get {cod_receta}\n")
        except:
            raise Http404
        ingredientereceta = self.get_object(receta)
        serializer = IngredientesRecetasSerializers(ingredientereceta)  
        return Response(serializer.data)
    def put(self, request, ingrecrec_fk, format=None):
        ingredientereceta = self.get_object(ingrecrec_fk)
        serializer = IngredientesRecetasSerializers(ingredientereceta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, ingrecrec_fk, format=None):
        ingredientereceta = self.get_object(ingrecrec_fk)
        ingredientereceta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
