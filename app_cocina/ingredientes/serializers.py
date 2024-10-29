from rest_framework import serializers
from .models import Temporadas, Ingredientes
class IngredientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes  
        exclude = ['is_removed', 'created', 'modified']
class TemporadasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Temporadas  
        exclude = ['is_removed', 'created', 'modified']