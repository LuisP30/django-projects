from django.test import TestCase
from ..models import Usuario


class UsuarioTesteCase(TestCase):

    def setUp(self):
        Usuario.objects.create(
            nome='Luis',
            email='luis@email.com',
            senha='1234'
        )

    def test_model_criado_no_banco(self):
        usuario = Usuario.objects.filter(nome='Luiss')
        self.assertFalse(usuario) # Verifica se o booleano de usuario é false

        # self.assertEqual(X, Y) # Verifica se X é igual a Y
        # self.assertNotEqual(X, Y) # Verifica se X é diferente de Y
        # self.assertTrue(X) # Verifica se o booleano de X é true
        # self.assertFalse(X) # Verifica se o booleano de X é false
        # self.assertIs(X, Y) # Verifica se X é Y
        # self.assertIsNot(X, Y) # Verifica se X não é Y
        # self.assertIsNone(X) # Verifica se X é nulo
        # self.assertIn(X, Y) # Verifica se X está em Y
        # self.assertNotIn(X, Y) # Verifica se X não está em Y
        # self.assertIsInstance(X, Y) Recebe um valor e uma classe. # Verifica se X é instância de Y
        # self.assertNotIsInstance(X, Y) Recebe um valor e uma classe. # Verifica se X não é instância de Y
        # self.assertGreater(X, Y) # Verifica se X é maior que Y
        # self.assertGreaterEqual(X, Y) # Verifica se X é maior ou igual a Y
        # self.assertLess(X, Y) # Verifica se X é menor que Y
        # self.assertLessEqual(X, Y) # Verifica se X é menor ou igual a Y

        # self.TemplateUsed(template) # Verifica se um template está sendo utilizado

    def test_add_pontos(self):
        usuario = Usuario.objects.get(nome='Luis')
        usuario.add_pontos()
        self.assertEqual(usuario.pontos, 10)