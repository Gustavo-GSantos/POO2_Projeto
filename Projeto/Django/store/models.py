from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=255, db_index=True)
    slugCategoria = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categorias"

    def get_absolute_url(self):
        return reverse("store:lista_categorias", args=[self.slugCategoria])

    def __str__(self) -> str:
        return self.nomeCategoria


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="produto", on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="criador_produto")
    nomeProduto = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, default='Administrador')
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='imagens/')
    slug = models.SlugField(max_length=255)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    em_estoque = models.BooleanField(default=True)
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Produtos'
        ordering = ('-criado',)

    def get_absolute_url(self):
        return reverse("store:detalhe_produto", args=[self.slug])

    def __str__(self) -> str:
        return self.nomeProduto
