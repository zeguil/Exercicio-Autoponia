from regadores.models import Regador
#DRF
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class RegadorSerializer(ModelSerializer):

    modelo = serializers.CharField(
        label="Modelo",
        help_text="Indica o modelo do regador."
    )

    capacidade = serializers.IntegerField(
        label="Capacidade",
        help_text="Indica a capacidade para armazenamento de água em mililitros."
    )
    pressao_bar = serializers.FloatField(
        label="Pressão da água",
        help_text="Indica a pressão da água"
    )
    ativo = serializers.BooleanField(
        label="Ativo",
        help_text="Indica se o regador esta ativo."
    )

    foto = serializers.ImageField(
        label="Foto",
        help_text="Uma foto do regador."
    )

    class Meta:
        model = Regador
        fields = ["modelo", "capacidade", "pressao_bar" "ativo", "foto", "planta"]