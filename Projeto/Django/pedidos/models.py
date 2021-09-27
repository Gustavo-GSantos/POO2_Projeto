from django.db import models
from django.conf import settings
from store.models import Produto

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedido_usuario')
    nome_completo = models.CharField(max_length=50)
    endereco = models.CharField(max_length=250)
    numero = models.CharField(max_length=250)
    cidade = models.CharField(max_length=100)
    numero_telefone = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    total_pago = models.DecimalField(max_digits=5, decimal_places=2)
    pedido_key = models.CharField(max_length=200)
    status_pagamento = models.BooleanField(default=False)

    class Meta:
        ordering = ('-criado',)
    
    def __str__(self):
        return str(self.criado)


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido,
                              related_name='items',
                              on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,
                                related_name='pedido_items',
                                on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

