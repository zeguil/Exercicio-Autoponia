from django.db import models

class Regador(models.Model):
    
    modelo = models.CharField(max_length=50)
    capacidade = models.FloatField()
    ativo = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='regadores', null=True, blank=True)

    class Meta:
        verbose_name = 'Regador'
        verbose_name_plural = 'Regadores'

    def __str__(self):
        return self.modelo