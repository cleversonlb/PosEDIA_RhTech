# Generated by Django 4.0.4 on 2022-05-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0006_alter_colaborador_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escolaridade',
            name='nivel_escolaridade',
            field=models.CharField(max_length=200),
        ),
    ]