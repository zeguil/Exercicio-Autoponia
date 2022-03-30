from regadores.models import Regador
from .serializers import RegadorSerializer
#DRF
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#Django-filter
from django_filters.rest_framework import DjangoFilterBackend

class RegadorViewSet(ModelViewSet):
    queryset = Regador.objects.all() 
    serializer_class = RegadorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['modelo']