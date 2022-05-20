from pyexpat import model
from tkinter import N
from django.db import models

# Create your models here.

class Departamento (models.Model):
    nome_depart = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_depart

class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    valor_hora = models.DecimalField(decimal_places=2, max_digits=10)

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} - Dep: {self.departamento.nome_depart}'

class Empresa (models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Departamento_Empresa (models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.empresa} - Dep: {self.departamento.nome_depart}'

class Escolaridade (models.Model):
    nivel_escolaridade = models.CharField(max_length=200)

    def __str__(self):
        return self.nivel_escolaridade
    

class Colaborador (models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    salario = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.nome

class Ponto (models.Model):
    entrada = models.DateTimeField('Entrada Data/Hora', null=True, blank=True)
    saida = models.DateTimeField('Saida Data/Hora', null=True, blank=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.colaborador.nome} - Data: {self.entrada}'

class Folha_Pagamento (models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    hora_extra = models.DecimalField(decimal_places=2 ,max_digits=5 )

class NF (models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    numero = models.IntegerField()
    dados = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    data_entrada = models.DateTimeField(auto_now=False, null=True, blank=True)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE, default= 'Choose')

    def __str__(self):
        return f'{self.numero} - Dep: {self.departamento.nome_depart} - Empresa: {self.empresa.nome} - Data: {self.data_entrada}'
        