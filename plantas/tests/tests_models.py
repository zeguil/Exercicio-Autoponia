from django.test import TestCase
from ..models import Planta

class PlantaTestCase(TestCase):
    def setUp(self):
        Planta.objects.create(
            nome = "alface",
            nome_cientifico = "Lactuca sativa",
            especie = "Roxo",
            grupo = "A",
            local = "porto alegre",
            iluminacao = "3h por dia",
            qtd_agua_dia = 300
        )

    def test_retorno_str(self):
        planta = Planta.objects.get(nome="alface")
        self.assertEquals(planta.__str__(), "alface")
