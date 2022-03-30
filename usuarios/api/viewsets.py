from usuarios.models import Usuario
from .serializers import UsuarioSerializer
#DRF
from rest_framework.viewsets import ModelViewSet
#Django-filter
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
    
