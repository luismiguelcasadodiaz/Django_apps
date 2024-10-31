from django.contrib import admin
from .models import Temporadas, Ingredientes, Categorias, Dificultades, Recetas, IngredientesRecetas
# Register your models here.
admin.site.register(Temporadas)
admin.site.register(Ingredientes)
admin.site.register(Categorias)
admin.site.register(Dificultades)
admin.site.register(Recetas)
admin.site.register(IngredientesRecetas)

