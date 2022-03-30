from usuarios.models import Usuario
from .serializers import UsuarioSerializer
#DRF
from rest_framework.viewsets import ModelViewSet

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

