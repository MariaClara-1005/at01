from django.db import models


class Cadastro(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

