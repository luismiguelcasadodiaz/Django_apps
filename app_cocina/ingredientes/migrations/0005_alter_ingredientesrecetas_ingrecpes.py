# Generated by Django 5.1.2 on 2024-10-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0004_categorias_dificultades_alter_temporadas_tempnom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientesrecetas',
            name='ingrecpes',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Peso en gramos'),
        ),
    ]