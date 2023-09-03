from django.db import models
from django.contrib import admin

# Criando as classes e linhas que receberão os dados.

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    id = models.AutoField(primary_key=True)
    choices_tipodeocorrencia = [
        ('ROUBO', 'Roubo'),
        ('FURTO', 'Furto'),
        ('HOMICIDE', 'Homicidio'),
    ]
    tipodeocorrencia = models.CharField(choices=choices_tipodeocorrencia, max_length=10)    
    pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE) # 'on_delete=models.CASCADE': ao remover uma pessoa, todos os seus relacionamentos tambem irao ser removidos
    oc_date = models.DateField(auto_now_add=True) # automaticamente insere a data que as informações foram postadas
    descricaoOcorrencia = models.CharField(max_length=500)

    def __str__(self):
        return f'Ocorrencia de {self.pessoa.nome}, CPF {self.pessoa.cpf}.'