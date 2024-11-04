from django.urls import path

from . import views

app_name = "webcook"

urlpatterns = [

    path("dificultades/", views.DificultadesView.as_view(), name="dificultades"),
    path("dificultades/<int:pk>/", views.DificultadesDetalleView.as_view(), name="dificultaddetalle"),
    path("temporadas/", views.TemporadasView.as_view(), name="temporadas"),
    path("temporadas/<int:pk>/", views.TemporadasDetalleView.as_view(), name="temporaddetalle"),
    path("categorias/", views.CategoriasView.as_view(), name="categorias"),
    path("categorias/<int:pk>/", views.CategoriasDetalleView.as_view(), name="categoriadetalle"),
    path("ingredientes/", views.IngredientesView.as_view(), name="ingredientes"),
    path("ingredientes/<int:pk>/", views.IngredientesDetalleView.as_view(), name="ingredientedetalle"),
    path("recetas/", views.RecetasView.as_view(), name="recetas"),
    path("recetas/<int:pk>/", views.RecetasDetalleView.as_view(), name="recetadetalle"),
 
]

"""
   # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
"""