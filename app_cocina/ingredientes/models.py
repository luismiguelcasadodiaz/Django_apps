from django.db import models

# Create your models here.
class Temporadas(models.Model):
    tempnom = models.CharField(verbose_name="Temporada", max_length=9)

    def __str__(self):
        return self.tempnom

class Ingredientes(models.Model):
    ingnom = models.CharField(verbose_name="Ingrediente", max_length=40)
    #ingtemp_fk = models.ForeignKey(Temporadas, on_delete=models.CASCADE, related_name="Temporada")
    ingtemp_fk = models.ForeignKey(Temporadas, on_delete=models.CASCADE, verbose_name = "Temporada")
    
    def __str__(self):
        return self.ingnom
    
class Categorias(models.Model):
    catnom = models.CharField(verbose_name="Categoría",max_length=10)

    def __str__(self):
        return self.catnom

class Dificultades(models.Model):
    difnom = models.CharField(verbose_name="Dificultad",max_length=10)

    def __str__(self):
        return self.difnom

class Recetas(models.Model):
    recnom = models.CharField(verbose_name="Receta", max_length=40)
    recela = models.CharField(verbose_name="Elaboración", max_length=400)
    rectem = models.IntegerField(verbose_name="Tiempo", default=0)
    recdif_fk = models.ForeignKey(Dificultades, on_delete=models.CASCADE, verbose_name="Dificultad")
    reccat_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="Temporada")

    def __str__(self):
        return f"{self.recnom} ({self.rectem} min)"

class IngredientesRecetas(models.Model):
    ingrecpes = models.PositiveSmallIntegerField(verbose_name="Peso en gramos",default=0, )
    ingrecing_fk = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, verbose_name="Ingrediente")
    ingrecrec_fk = models.ForeignKey(Recetas, on_delete=models.CASCADE, verbose_name="Receta")
    
    def __str__(self):
        return f"{self.ingrecrec_fk} - {self.ingrecing_fk} : {self.ingrecpes} gramos"