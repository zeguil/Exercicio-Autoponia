from django.db import models
from plantas.models import Planta

class Regador(models.Model):
    
    modelo = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    ativo = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='regadores', null=True, blank=True)
    planta = models.ManyToManyField(Planta, blank=True)

    class Meta:
        verbose_name = 'Regador'
        verbose_name_plural = 'Regadores'

    def __str__(self):
        return self.modelo