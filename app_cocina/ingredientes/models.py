from django.db import models

# Create your models here.
class Temporadas(models.Model):
    tempnom = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.tempnom}"


class Ingredientes(models.Model):
    ingnom = models.CharField(max_length=40)
    ingtemp_fk = models.ForeignKey(Temporadas, on_delete=models.CASCADE)

