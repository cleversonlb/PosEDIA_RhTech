# Generated by Django 4.0.4 on 2022-05-20 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0011_alter_nf_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='folha_pagamento',
            name='data_lancamento',
            field=models.DateField(blank=True, null=True),
        ),
    ]