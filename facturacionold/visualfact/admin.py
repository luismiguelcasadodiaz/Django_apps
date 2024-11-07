from django.contrib import admin

# Register your models here.
from .models import Facturas, Detalles

# Register your models here.
admin.site.register(Facturas)
admin.site.register(Detalles)