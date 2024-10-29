from rest_framework import serializers
from django.db import models
from .models import Temporadas, Ingredientes
class IngredientesSerializers(serializers.ModelSerializer):
    ingnom = serializers.CharField(max_length=40)
    ingtemp_fk = serializers.CharField(max_length=9)
    class Meta:
        model = Ingredientes
        fields = '__all__'
        #exclude = ['is_removed', 'created', 'modified']
class TemporadasSerializers(serializers.ModelSerializer):
    tempnom = serializers.CharField(max_length=10)
    class Meta:
        model = Temporadas  
        fields ='__all__'
        #exclude = ['is_removed', 'created', 'modified']