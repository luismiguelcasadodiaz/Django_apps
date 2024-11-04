from django.urls import path

from . import views

app_name = "ingredientes"

urlpatterns = [
    path('ingredientes', views.Ingredientes_APIView.as_view()), 
    path('ingredientes/<int:pk>/', views.Ingredientes_APIView_Detail.as_view()),
    path('temporadas', views.Temporadas_APIView.as_view(), name='create_temporada'), 
    path('temporadas/<int:pk>/', views.Temporadas_APIView_Detail.as_view()), 
    path('dificultades', views.Dificultades_APIView.as_view()), 
    path('dificultades/<int:pk>/', views.Dificultades_APIView_Detail.as_view()), 
    path('categorias', views.Categorias_APIView.as_view()), 
    path('categorias/<int:pk>/', views.Categorias_APIView_Detail.as_view()),
    path('recetas', views.Recetas_APIView.as_view()), 
    path('recetas/<int:pk>/', views.Recetas_APIView_Detail.as_view()),
    path('ingredientesrecetas', views.IngredientesRecetas_APIView.as_view()), 
    path('ingredientesrecetas/<str:ingrecrec_fk>/', views.IngredientesRecetas_APIView_Detail.as_view())   
]  