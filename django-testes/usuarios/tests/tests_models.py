from django.test import TestCase
from ..models import Usuario

class UsuarioTesteCase(TestCase):
    
    def setUp(self):
        Usuario.objects.create(
            nome = 'Luis',
            email = 'luis@email.com',
            senha = '1234'
        )
    
    def test_model_criado_no_banco(self):
        usuario = Usuario.objects.get(nome = 'Luis')
        
        self.assertEqual(usuario.__str__(), 'Luis')
        
    def test_add_pontos(self):
        usuario = Usuario.objects.get(nome = 'Luis')
        usuario.add_pontos()
        self.assertEqual(usuario.pontos, 10)