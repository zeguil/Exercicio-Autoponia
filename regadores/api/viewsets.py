from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from regadores.models import Regador
from .serializers import RegadorSerializer

class RegadorViewSet(ModelViewSet):
    queyset = Regador.objects.all()
    serializer_class = RegadorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )