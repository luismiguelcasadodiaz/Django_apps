from django.db import models

# Create your models here.
class Temporadas(models.Model):
    tempnom = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.tempnom}"

class Ingredientes(models.Model):
    ingnom = models.CharField(max_length=40)
    #ingtemp_fk = models.ForeignKey(Temporadas, on_delete=models.CASCADE, related_name="Temporada")
    ingtemp_fk = models.ForeignKey(Temporadas, on_delete=models.CASCADE)

class Categorias(models.Model):
    catnom = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.catnom}"

class Dificultades(models.Model):
    difnom = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.difnom}"

class Recetas(models.Model):
    recnom = models.CharField(max_length=40)
    recela = models.CharField(max_length=400)
    rectem = models.IntegerField(default=0)
    recdif_fk = models.ForeignKey(Dificultades, on_delete=models.CASCADE)
    reccat_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE)

class IngredientesRecetas(models.Model):
    ingrecpes = models.PositiveSmallIntegerField(verbose_name="Peso en gramos",default=0, )
    ingrecing_fk = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    ingrecrec_fk = models.ForeignKey(Recetas, on_delete=models.CASCADE)
