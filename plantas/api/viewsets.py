import requests
from plantas.models import Planta
from .serializers import PlantaSerializer
#DRF
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#Django-filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.http import JsonResponse

class PlantaViewSet(ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']

    # rota personalizada
    @action(methods=['GET'], detail=True)
    def clima(self, request, pk=None):
        obj = self.get_object()
        cidade = obj.local

        # chave da API do OpenWeather
        API_KEY = "ebe9323dd4d66a4bb1b75ea1fc85302c"
        # requisção passando o nome da cidade e a chave da api
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        #Armazeno as informações mais importantes 
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        temp_min = requisicao_dic['main']['temp_min'] - 273.15
        temp_max = requisicao_dic['main']['temp_max'] - 273.15
        umidade = requisicao_dic['main']['humidity']

        #Construo o Json
        data = {
            "local": cidade,
            "clima" : descricao.title(),
            "temperatura": f"{temperatura:.0f}",
            "temperatura_maxima": f"{temp_max:.0f}",
            "temperatura_minima": f"{temp_min:.0f}",
            "umidade": umidade
        }
        return JsonResponse(data)
            