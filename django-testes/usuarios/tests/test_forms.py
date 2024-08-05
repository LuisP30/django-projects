from django.test import TestCase
from ..form import UsuarioForm
from django.http import HttpRequest

class FormsTestCase(TestCase):
    
    def setUp(self):
        self.form = UsuarioForm()
        
    def test_campos_form(self):
        # Verificando se o form possui os campos do model
        self.assertIn('nome', self.form.fields)
        self.assertIn('email', self.form.fields)
        self.assertIn('senha', self.form.fields)
        self.assertIn('pontos', self.form.fields)
        
    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            "nome": 'Luis',
            "email": 'luis@gmail.com',
            "senha": '1234',
            "pontos": 0
        }
        form = UsuarioForm(request.POST)
        self.assertTrue(form.is_valid())