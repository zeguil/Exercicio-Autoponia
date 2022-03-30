import requests
from django.db import models
from django.http import JsonResponse
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

    @action(methods=['GET'], detail=True)
    def tempo(self, request, **kwargs):
        cidade = self.tempo

        API_KEY = "ebe9323dd4d66a4bb1b75ea1fc85302c"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        data = {"clima" : descricao.title(), "temperatura": f"{temperatura:.0f}"}
        return JsonResponse(data)