from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nomeCategoria', 'slugCategoria']
    prepopulated_fields = {'slugCategoria': ('nomeCategoria',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nomeProduto', 'autor', 'slug', 'preco', 'em_estoque', 'criado', 'atualizado']
    list_filter = ['em_estoque', 'disponivel']
    list_editable = ['preco', 'em_estoque']
    prepopulated_fields = {'slug': ('nomeProduto',)}
