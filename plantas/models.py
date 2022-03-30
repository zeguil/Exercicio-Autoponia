from django.db import models

class Planta(models.model):

    Tipos_de_reino = (
      (1, 'briófitas'),
      (2, 'angiospermas'),
      (3, 'pteridófitas'),
      (4, 'gimnospermas'),
    )
    
    nome = models.CharField(max_length=45)
    nome_cientifico = models.models.CharField(max_length=50)
    especie = models.CharField(max_length=45)
    reino = models.PositiveSmallIntegerField(choices=Tipos_de_reino)
    horas_de_luz = models.DurationField()
    qtd_agua_dia = models.FloatField()
    foto = models.ImageField(upload_to='plantas', null=True, blank=True)

    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'

    def __str__(self):
        return self.nome