# Generated by Django 4.0.4 on 2022-05-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0002_alter_nf_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='escolaridade',
            name='nivel_escolaridade',
            field=models.CharField( max_length=200),
        ),
    ]