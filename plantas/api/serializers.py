from regadores.models import Planta
#DRF
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class PlantaSerializer(ModelSerializer):

    nome = serializers.CharField(
        label="Nome",
        help_text="Indica o nome da planta"
    )

    nome_cientifico = serializers.CharField(
        label="Nome Científico",
        help_text="Indica o nome científico da planta"
    )
    especie = serializers.CharField(
        label="Espécie",
        help_text="Indica a espécie da planta"
    )

    reino = serializers.PositiveSmallIntegerField(
        label="Reino",
        help_text="Indica o reino da planta"
    )

    horas_de_luz = serializers.DurationField(
        label="Horas na luz",
        help_text="Indica o tempo de luz que a planta deve receber"
    )

    qtd_agua_dia = serializers.FloatField(
        label="Quantidade de água",
        help_text="Indica a quantidade de água que a planta deve receber"
    )

    foto = serializers.ImageField(
        label="Foto",
        help_text="Uma foto da planta"
    )

    class Meta:
        model = Planta
        fields = ["nome", "nome_cientifico", "especie", "reino", "horas_de_luz", "qtd_agua_dia", "foto"]