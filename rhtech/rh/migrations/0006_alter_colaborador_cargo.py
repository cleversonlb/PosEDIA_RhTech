# Generated by Django 4.0.4 on 2022-05-19 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0005_remove_colaborador_departamento_colaborador_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.cargo'),
        ),
    ]