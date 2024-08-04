from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ..models import Usuario


class ViewsTesteCase(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome='Luis',
            email='luis@email.com',
            senha='1234'
        )
        self.client = Client() # Para fazer requisição
        self.url = reverse('home')

    def test_status_code_200(self):
        # response = self.client.get(f'{self.url}?id=1')  # Estou fazendo uma requisição GET enviando parâmetro
        response = self.client.get(f'{self.url}?email=luis@email.com')
        self.assertEqual(response.status_code, 200)  # Testando se o status code para a view de home foi 200

    def test_status_code_404(self):
        response = self.client.get(f'{self.url}?email=email@email.com') # Passando o email errado e esperando um erro
        self.assertEqual(response.status_code, 404)  # Testando se o status code para a view de home foi 404
        