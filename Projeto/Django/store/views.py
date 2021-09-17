from django.shortcuts import get_object_or_404, render

from .models import Categoria, Produto


def categorias(request):
    return {
        'categorias': Categoria.objects.all()
    }


def todosOsProdutos(request):
    produtos = Produto.objects.all()
    return render(request, 'store/home.html', {'produtos': produtos})


def detalhe_produto(request, slug):
    produto = get_object_or_404(Produto, slug=slug, em_estoque=True)
    return render(request, 'store/produtos/detalhes.html', {'produto': produto})


def lista_categorias(request, slug_categorias):
    categoria = get_object_or_404(Categoria, slugCategoria=slug_categorias)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'store/produtos/categoria.html', {'categoria': categoria, 'produtos': produtos})
