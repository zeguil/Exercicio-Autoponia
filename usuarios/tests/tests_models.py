from django.test import TestCase
from ..models import Usuario

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            username = "Alvaro",
            password = "autoponia123",
            email = None,
            is_staff = True,
            is_superuser = True,
        )
        
    def test_retorno_str(self):
        usuario = Usuario.objects.get(username="Alvaro")
        self.assertEquals(usuario.__str__(), "Alvaro")
