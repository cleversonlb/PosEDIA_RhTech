# Generated by Django 4.0.4 on 2022-05-20 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0010_nf_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nf',
            name='departamento',
            field=models.ForeignKey(default='Choose', on_delete=django.db.models.deletion.CASCADE, to='rh.departamento'),
        ),
    ]