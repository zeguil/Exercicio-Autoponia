from regadores.models import Regador
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class RegadorSerializer(ModelSerializer):
    
    modelo = serializers.CharField(
        label="Modelo",
        help_text="Indica o modelo do regador"
    )

    capacidade = serializers.DurationField(
        label="Capacidade",
        help_text="Indica a capacidade para armazenamento de água"
    )

    ativo = serializers.BooleanField(
        label="Ativo",
        help_text="Indica se o regador esta ativo"
    )

    foto = serializers.ImageField(
        label="Foto",
        help_text="Uma foto do regador"
    )

    class Meta:
        model = Regador
        fields = ["modelo", "capacidade", "ativo", "foto"]