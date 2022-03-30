from django.db import models

class Regador(models.model):
    nome = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    qtd_agua = models.FloatField()
    foto = models.models.ImageField(upload_to='regadores', null=True, blank=True)

    class Meta:
        verbose_name = 'Regador'
        verbose_name_plural = 'Regadores'

    def __str__(self):
        return self.nome