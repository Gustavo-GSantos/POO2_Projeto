from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .carrinho import Carrinho
from store.models import Produto

def carrinho_resumo(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho/resumo.html', {'carrinho': carrinho})


def carrinho_add(request):
    carrinho = Carrinho(request)

    if request.POST.get('action') == 'post':
        produto_id = int(request.POST.get('produtoid'))
        produto_qtd = int(request.POST.get('produtoqtd'))
        produto = get_object_or_404(Produto, id=produto_id)
        carrinho.add(produto=produto, qtd=produto_qtd)

        carrinhoqtd = carrinho.__len__()
        response = JsonResponse({'qtd': carrinhoqtd})
        return response

def carrinho_delete(request):
    carrinho = Carrinho(request)

    if request.POST.get('action') == 'post':
        produto_id = int(request.POST.get('produtoid'))
        carrinho.delete(produto=produto_id)

        carrinhoqtd = carrinho.__len__()
        totalcarrinho = carrinho.get_total_price()
        response = JsonResponse({'qtd': carrinhoqtd, 'subtotal': totalcarrinho})
        return response
    
def carrinho_update(request):
    carrinho = Carrinho(request)
    
    if request.POST.get('action') == 'post':
        produto_id = int(request.POST.get('produtoid'))
        produto_qtd = int(request.POST.get('produtoqtd'))
        carrinho.update(produto=produto_id, qtd=produto_qtd)

        carrinhoqtd = carrinho.__len__()
        totalcarrinho = carrinho.get_total_price()
        response = JsonResponse({'qtd': carrinhoqtd, 'subtotal': totalcarrinho})
        return response

def pedido_confirmado(request):
    carrinho = Carrinho(request)
    carrinho.clear()
    return render(request, 'pedidoconfirmado.html')