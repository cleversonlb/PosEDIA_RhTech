# Generated by Django 4.0.4 on 2022-05-19 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0004_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='departamento',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='cargo',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='rh.cargo'),
        ),
    ]
