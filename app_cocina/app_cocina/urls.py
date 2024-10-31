"""app_cocina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ingredientes.views import *


app_name = 'ingredientes'
urlpatterns = [
    path('admin', admin.site.urls),
    path('ingredientes', Ingredientes_APIView.as_view()), 
    path('ingredientes/<int:pk>/', Ingredientes_APIView_Detail.as_view()),
    path('temporadas', Temporadas_APIView.as_view(), name='create_temporada'), 
    path('temporadas/<int:pk>/', Temporadas_APIView_Detail.as_view()), 
    path('dificultades', Dificultades_APIView.as_view()), 
    path('dificultades/<int:pk>/', Dificultades_APIView_Detail.as_view()), 
    path('categorias', Categorias_APIView.as_view()), 
    path('categorias/<int:pk>/', Categorias_APIView_Detail.as_view()),
    path('recetas', Recetas_APIView.as_view()), 
    path('recetas/<int:pk>/', Recetas_APIView_Detail.as_view()),
    path('ingredientesrecetas', IngredientesRecetas_APIView.as_view()), 
    path('ingredientesrecetas/<str:ingrecrec_fk>/', IngredientesRecetas_APIView_Detail.as_view())   
]   