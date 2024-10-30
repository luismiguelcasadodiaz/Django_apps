from rest_framework import serializers
from django.db import models
from .models import Temporadas, Ingredientes, Dificultades, Categorias, Recetas, IngredientesRecetas
class IngredientesSerializers(serializers.ModelSerializer):
    ingnom = serializers.CharField(max_length=40)
    ingtemp_fk = serializers.SlugRelatedField(queryset=Temporadas.objects.all(),slug_field='tempnom')
    class Meta:
        model = Ingredientes
        fields = '__all__'

class TemporadasSerializers(serializers.ModelSerializer):
    tempnom = serializers.CharField(max_length=9)
    class Meta:
        model = Temporadas  
        fields ='__all__'

class DificultadesSerializers(serializers.ModelSerializer):
    difnom = serializers.CharField(max_length=10)
    class Meta:
        model = Dificultades  
        fields ='__all__'

class CategoriasSerializers(serializers.ModelSerializer):
    catnom = serializers.CharField(max_length=10)
    class Meta:
        model = Categorias  
        fields ='__all__'

class RecetasSerializers(serializers.ModelSerializer):
    recnom = serializers.CharField(max_length=40)
    recela = serializers.CharField(max_length=400)
    rectem = serializers.IntegerField()
    recdif_fk = serializers.SlugRelatedField(queryset=Dificultades.objects.all(),slug_field='difnom')
    reccat_fk = serializers.SlugRelatedField(queryset=Categorias.objects.all(),slug_field='catnom')

    class Meta:
        model = Recetas  
        fields ='__all__'