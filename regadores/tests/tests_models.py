from django.test import TestCase
from ..models import Regador

class RegadorTestCase(TestCase):
    def setUp(self):
        Regador.objects.create(
            modelo = "manual",
            capacidade = 600,
            pressao_bar = 5,
            ativo = True,
            
        )
        
    def test_retorno_str(self):
        regador = Regador.objects.get(modelo="manual")
        self.assertEquals(regador.__str__(), "manual")
