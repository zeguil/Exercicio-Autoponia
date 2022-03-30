from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from plantas.models import Planta
from .serializers import PlantaSerializer

class PlantaViewSet(ModelViewSet):
    queyset = Planta.objects.all()
    serializer_class = PlantaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )