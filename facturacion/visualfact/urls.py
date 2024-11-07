from django.contrib import admin
from django.urls import path
from visualfact import views

app_name = 'visualfact'
urlpatterns = [
    path('facturas/', views.FacturasView.as_view(), name="facturas"),
    path('facturadetalle/<int:pk>/', views.FacturaDetalleView.as_view(), name="facturadetalle")
]   

