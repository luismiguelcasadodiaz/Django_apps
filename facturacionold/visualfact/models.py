from django.db import models

# Create your models here.
class Facturas(models.Model):
    TIPO_FACTURA = [
        ("V", "Vencida"),
        ("C", "Cobrada"),
        ("P", "Pendiente"),
    ]
    factcli = models.CharField(max_length=50, verbose_name="Cliente")
    factfec = models.DateField(verbose_name =  "Fecha Factura")
    factest = models.CharField(max_length=1, verbose_name="Estado", choices=TIPO_FACTURA)
    factdir = models.CharField(max_length=50, verbose_name="Direccion")
    factmai = models.EmailField()
    factcre = models.DateTimeField(verbose_name =  "Fecha registro", auto_now_add=True)
    factmod = models.DateTimeField(verbose_name =  "Fecha modifica", auto_now=True)

    def __str__(self):
        s = self.factfec.strftime("%y%m%d")
        result = f"{s}_{self.factcli}"
        return result

class Detalles(models.Model):
    class Type(models.TextChoices):
        TIPO1 = 1
        TIPO2 = 2
        TIPO3 = 3

    dettip = models.CharField(max_length=6, choices=Type.choices, verbose_name="Producto Tipo")
    detnom = models.CharField(max_length=50, verbose_name="Producto")
    detpre = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio")
    factura = models.ForeignKey(Facturas, on_delete=models.CASCADE)
    detiva = models.GeneratedField(models.F('price') * 0.21, output_field=models.DecimalField(max_digits=10, decimal_places=2),db_persist=False )

        
    def __str__(self):
        return f"{self.detnom}-{self.factura}"