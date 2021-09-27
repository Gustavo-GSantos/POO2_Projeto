from django.http.response import JsonResponse
from django.shortcuts import render

from carrinho.carrinho import Carrinho

from .models import Pedido, PedidoItem

def add(request):
    carrinho = Carrinho(request)
    if request.POST.get('action') == 'post':
        pedido_key = request.POST.get('pedido_key')
        usuario_id = request.usuario.id
        carrinho_total = carrinho.get_total_price

        if Pedido.objects.filter(pedido_key=pedido_key).exists():
            pass
        else:
            pedido = Pedido.objects.create(usuario_id=usuario_id, nome_completo='nome', endereco='endereco',
                                            numero='numero', total_pago=carrinho_total, pedido_key=pedido_key)
            pedido_id = pedido.pk

            for item in carrinho:
                PedidoItem.objects.create(pedido_id=pedido_id, produto=item['produto'], preco=item['preco'],
                                        quantidade=item['qtd'])
        
        response = JsonResponse({'sucess': 'retornar response'})
        return response
    
def confirmar_pagamento(data):
    Pedido.objects.filter(pedido_key=data).update(status_pagamento=True)

def usuario_pedidos(request):
    usuario_id = request.user.id
    pedidos = Pedido.objects.filter(usuario_id=usuario_id).filter(status_pagamento=True)
    return pedidos