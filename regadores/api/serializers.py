from regadores.models import Regador
from rest_framework.serializers import ModelSerializer

class RegadorSerializer(ModelSerializer):
    class Meta:
        model = Regador
        fields = "__all__"