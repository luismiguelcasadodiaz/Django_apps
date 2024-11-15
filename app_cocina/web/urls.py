from django.urls import path

from web import views

app_name = "web"

urlpatterns = [

    #path("dificultades/", views.DificultadesView.as_view(), name="dificultades"),
    #path("dificultades/<int:pk>/", views.DificultadesDetalleView.as_view(), name="dificultaddetalle"),
    #path("temporadas/", views.TemporadasView.as_view(), name="temporadas"),
    #path("temporadas/<int:pk>/", views.TemporadasDetalleView.as_view(), name="temporaddetalle"),
    path("categorias/", views.CategoriasView.as_view(), name="categorias"),
    path("categorias/<int:pk>/", views.CategoriasDetalleView.as_view(), name="categoriadetalle"),
    #path("ingredientes/", views.IngredientesView.as_view(), name="ingredientes"),
    #path("ingredientes/<int:pk>/", views.IngredientesDetalleView.as_view(), name="ingredientedetalle"),
    #path("recetas/", views.RecetasView.as_view(), name="recetas"),
    #path("recetas/<int:pk>/", views.RecetasDetalleView.as_view(), name="recetadetalle"),
    path("testcat/", views.testcat, name="test"),
    path("testing/", views.testing, name="test"),
    path("recetaspordificultad/<int:pk>/", views.one_to_many, name = "one_to_many"),
    path("chart/", views.chart, name="chart1")
 
]