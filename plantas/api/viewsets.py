from plantas.models import Planta
from .serializers import PlantaSerializer
#DRF
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#Django-filter
from django_filters.rest_framework import DjangoFilterBackend

class PlantaViewSet(ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']
    