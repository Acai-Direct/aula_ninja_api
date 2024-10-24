from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique= False)
    senha = models.CharField(max_length=100)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome

