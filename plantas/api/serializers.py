from regadores.models import Planta
from rest_framework.serializers import ModelSerializer

class PlantaSerializer(ModelSerializer):
    class Meta:
        model = Planta
        fields = "__all__"