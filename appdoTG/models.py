#Importa o módulo models
from django.db import models

# Definir o modelo TiquinhoStats
class TiquinhoStats(models.Model):
    # Campos do modelo TiquinhoStats
    título = models.CharField(max_length=50)  # Campo de caractere com no máximo 50 caracteres
    números = models.TextField()  # Campo de texto
    tipo = models.TextField()  # Campo de texto
    essa_temporada = models.BooleanField()  # Campo booleano (verdadeiro ou falso)

# Definição do modelo TiquinhoTeams
class TiquinhoTeams(models.Model):
    # Campos do modelo TiquinhoTeams
    título = models.CharField(max_length=50)  # Campo de caractere com no máximo 50 caracteres
    time = models.TextField()  # Campo de texto
    gols = models.TextField()  # Campo de texto
    clube_atual = models.BooleanField()  # Campo booleano (verdadeiro ou falso)

