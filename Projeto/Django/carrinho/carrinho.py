from store.models import Produto
from decimal import Decimal


class Carrinho():
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('skey')
        if 'skey' not in request.session:
            carrinho = self.session['skey'] = {}
        self.carrinho = carrinho
        
    def add(self, produto, qtd):
        produto_id = str(produto.id)

        if produto_id in self.carrinho:
            self.carrinho[produto_id]['qtd'] = qtd
        else:
            self.carrinho[produto_id] = {'preco': str(produto.preco), 'qtd': qtd}

        self.save()

    def __iter__(self):
        produto_ids = self.carrinho.keys()
        produtos = Produto.produtos.filter(id__in=produto_ids)
        carrinho = self.carrinho.copy()

        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
        
        for item in carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['preco_total'] = item['preco'] * item['qtd']
            yield item
        
    def __len__(self):
        return sum(item['qtd'] for item in self.carrinho.values())
    
    def update(self, produto, qtd):
        produto_id = str(produto)

        if produto_id in self.carrinho:
            self.carrinho[produto_id]['qtd'] = qtd

        self.save()
    
    def get_total_price(self):
        return sum(Decimal(item['preco']) * item['qtd'] for item in self.carrinho.values())

    def get_subtotal_price(self):
        return sum(Decimal(item['preco']) * item['qtd'] for item in self.carrinho.values())

    def delete(self, produto):
        produto_id = str(produto)
        
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            print(produto_id)
            self.save()

    def clear(self):
        from django.conf import settings
        del self.session[settings.ID_SESSAO_CARRINHO]
        self.save()

    def save(self):
        self.session.modified = True

    def carrinho(request):
        return {'carrinho': Carrinho(request)}