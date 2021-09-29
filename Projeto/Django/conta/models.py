from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class GerenciadorContas(BaseUserManager):
    def create_superuser(self, email, user_name, password, **outros_campos):
        outros_campos.setdefault('is_staff', True)
        outros_campos.setdefault('is_superuser', True)
        outros_campos.setdefault('is_active', True)

        if outros_campos.get('is_staff') is not True:
            raise ValueError(
                'Superuser tem que designado para o atributo is_staff=True')
        if outros_campos.get('is_superuser') is not True:
            raise ValueError(
                'Superuser tem que designado para o atributo is_superuser=True')
        
        return self.criar_usuario(email, user_name, password, **outros_campos)
    
    def criar_usuario(self, email, user_name, password, **outros_campos):
        if not email:
            raise ValueError(_('O email é um campo obrigatório!'))
        
        email = self.normalize_email(email)
        usuario = self.model(email=email, user_name=user_name, **outros_campos)
        usuario.set_password(password)
        usuario.save()
        return usuario


class BaseDeUsuarios(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True)
    user_name = models.CharField(max_length=140, unique=True)
    primeiro_nome = models.CharField(max_length=140, blank=True)
    
    pais = CountryField()
    numero_telefone = models.CharField(max_length=13, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    endereco = models.CharField(max_length=140, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    cidade = models.CharField(max_length=140, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    objects = GerenciadorContas()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = "Contas"
        verbose_name_plural = "Contas"
    
    def email_usuario(self, assunto, mensagem):
        send_mail(
            assunto,
            mensagem,
            'a@a.com',
            [self.email],
            fail_silently=False,)

    def __str__(self):
        return self.user_name
