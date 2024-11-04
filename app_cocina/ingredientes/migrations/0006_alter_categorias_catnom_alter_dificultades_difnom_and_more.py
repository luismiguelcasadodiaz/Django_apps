# Generated by Django 5.1 on 2024-11-03 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0005_alter_ingredientesrecetas_ingrecpes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='catnom',
            field=models.CharField(max_length=10, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='dificultades',
            name='difnom',
            field=models.CharField(max_length=10, verbose_name='Dificultad'),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='ingnom',
            field=models.CharField(max_length=40, verbose_name='Ingrediente'),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='ingtemp_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.temporadas', verbose_name='Temporada'),
        ),
        migrations.AlterField(
            model_name='ingredientesrecetas',
            name='ingrecing_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.ingredientes', verbose_name='Ingrediente'),
        ),
        migrations.AlterField(
            model_name='ingredientesrecetas',
            name='ingrecrec_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.recetas', verbose_name='Receta'),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='reccat_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.categorias', verbose_name='Temporada'),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='recdif_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.dificultades', verbose_name='Dificultad'),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='recela',
            field=models.CharField(max_length=400, verbose_name='Elaboración'),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='recnom',
            field=models.CharField(max_length=40, verbose_name='Receta'),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='rectem',
            field=models.IntegerField(default=0, verbose_name='Tiempo'),
        ),
        migrations.AlterField(
            model_name='temporadas',
            name='tempnom',
            field=models.CharField(max_length=9, verbose_name='Temporada'),
        ),
    ]
