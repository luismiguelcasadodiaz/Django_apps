from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import IngredientesSerializers, TemporadasSerializers, CategoriasSerializers, CategoriasSerializers, RecetasSerializers
from .models import Ingredientes, Temporadas, Dificultades, Categorias, Recetas
from rest_framework import status
from django.http import Http404
# Create your views here.

    
class Ingredientes_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        ingrediente = Ingredientes.objects.all()
        serializer = IngredientesSerializers(ingrediente, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = IngredientesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Ingredientes_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Ingredientes.objects.get(pk=pk)
        except Ingredientes.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        serializer = IngredientesSerializers(ingrediente)  
        return Response(serializer.data)
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
    
class Temporadas_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        temporada = Temporadas.objects.all()
        serializer = TemporadasSerializers(temporada, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = TemporadasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Temporadas_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Temporadas.objects.get(pk=pk)
        except Temporadas.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        temporada = self.get_object(pk)
        serializer = TemporadasSerializers(temporada)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        temporada = self.get_object(pk)
        serializer = TemporadasSerializers(temporada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        temporada = self.get_object(pk)
        temporada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Dificultades_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        dificultades = Dificultades.objects.all()
        serializer = DificultadesSerializers(dificultades, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = DificultadesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Dificultades_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Dificultades.objects.get(pk=pk)
        except Dificultades.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        dificultad = self.get_object(pk)
        serializer = DificultadesSerializers(dificultad)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        dificultad = self.get_object(pk)
        serializer = DificultadesSerializers(dificultad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        dificultad = self.get_object(pk)
        dificultad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Categorias_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        categorias = Categorias.objects.all()
        serializer = CategoriasSerializers(categorias, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CategoriasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Categorias_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Categorias.objects.get(pk=pk)
        except Categorias.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriasSerializers(categoria)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriasSerializers(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
