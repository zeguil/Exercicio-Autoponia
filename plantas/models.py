import requests
from django.db import models
from rest_framework.decorators import action

class Planta(models.Model):

    GRUPO_CHOICES = (
      ('B', 'briófitas'),
      ('A','angiospermas'),
      ('P','pteridófitas'),
      ('G','gimnospermas'),
    )

    nome = models.CharField(max_length=45)
    nome_cientifico = models.CharField(max_length=50)
    especie = models.CharField(max_length=45)
    grupo = models.CharField(max_length=1, choices=GRUPO_CHOICES)
    local = models.CharField(max_length=15)
    iluminacao = models.TextField()
    qtd_agua_dia = models.FloatField()
    foto = models.ImageField(upload_to='plantas', null=True, blank=True)

    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'

    def __str__(self):
        return self.nome