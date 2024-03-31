from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.safestring import mark_safe

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Cargos(models.Model):
    nome = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Pessoa(AbstractBaseUser, PermissionsMixin):
    imagem = models.ImageField(upload_to='users-img')
    nome = models.CharField(max_length=50, blank=False, null=False)
    sobrenome = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    cargo = models.ManyToManyField(Cargos)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome', 'password')

    def __str__(self):
        return self.nome

    def get_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @mark_safe
    def get_image(self):
        return f'<img width="30px" src="/media/{self.imagem}">'

class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome