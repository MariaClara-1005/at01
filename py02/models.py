from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=300, unique=True)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self):
        return self.name

