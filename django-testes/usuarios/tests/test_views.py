from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ..models import Usuario
from django.contrib.messages import get_messages


class ViewsTesteCase(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome='Luis',
            email='luis@gmail.com',
            senha='1234'
        )
        self.client = Client() # Para fazer requisição
        self.url = reverse('home')

    def test_status_code_200(self):
        # response = self.client.get(f'{self.url}?id=1')  # Estou fazendo uma requisição GET enviando parâmetro
        response = self.client.get(f'{self.url}?email=luis@gmail.com')
        self.assertEqual(response.status_code, 200)  # Testando se o status code para a view de home foi 200

    def test_status_code_404(self):
        response = self.client.get(f'{self.url}?email=email@gmail.com') # Passando o email errado e esperando um erro
        self.assertEqual(response.status_code, 404)  # Testando se o status code para a view de home foi 404
        
    def test_template_used_home_cond_1(self):
        response = self.client.get(f'{self.url}?email=luis@gmail.com&cond=1')
        self.assertTemplateUsed(response, 'home.html') # Se cond = 1 então renderiza home (lógica da view)
        
    def test_template_used_home_cond_2(self):
        response = self.client.get(f'{self.url}?email=luis@gmail.com&cond=2')
        self.assertTemplateUsed(response, 'logar.html') # Se cond = 2 então renderiza logar
        
    def test_message_error_email_gmail(self):
        response = self.client.get(f'{self.url}?email=luis@email.com&cond=2')
        messages = [m.message for m in get_messages(response.wsgi_request)] # ESTUDAR list comprehension
        self.assertIn('Informe um email do G-mail', messages) # Verificando se essa string está em messages