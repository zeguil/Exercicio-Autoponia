from plantas.models import Planta
from .serializers import PlantaSerializer
#DRF
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PlantaViewSet(ModelViewSet):
    queyset = Planta.objects.all()
    serializer_class = PlantaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )