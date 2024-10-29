# Generated by Django 4.1 on 2024-10-29 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temporadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempnom', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingnom', models.CharField(max_length=40)),
                ('ingtemp_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.temporadas')),
            ],
        ),
    ]
