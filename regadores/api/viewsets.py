from regadores.models import Regador
from .serializers import RegadorSerializer
#DRF libs
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RegadorViewSet(ModelViewSet):
    queyset = Regador.objects.all() 
    serializer_class = RegadorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )