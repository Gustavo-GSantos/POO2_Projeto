#Primeiras classes e métodos identificados

class Cliente:

    # Deve conter informações que identifiquem o cliente
    # Nome, telefone, endereço(pra entrega)

    def __init__(self):
        pass

    def criar_cliente(self, nome_cliente, telefone_cliente, endereco_cliente):
        self.nome_cliente = nome_cliente
        self.telefone_cliente = telefone_cliente
        self.endereco_cliente = endereco_cliente
    
    def retorna_nome_cliente(self): #função para usar o nome do cliente no pedido
        return self.nome_cliente    #pra ter uma rápida noção de quem é
        
    def retorna_info_cliente(self):
        #TODO: Como retornar todas as informações do cliente? É possível ou melhor 3 métodos diferentes?

        #O objetivo de retornar todas as informações de uma vez é pra mostrar
        #a informação completa e saber exatamente quem é o cliente

class Mascara: #TODO: Mudar nome pra class Tecido? Já que os primeiros métodos são mais focados nisso
               #TODO: e considerando que as máscaras tem outros atributos como preço e tamanho

    # Deve conter informações sobre as máscaras, podendo 
    # adicionar novos tecidos
    # Valores serão fixos (tipo1 = 5 reais, tipo2 = 10 reais)

    def __init__(self):
        pass
    
    def novo_tecido(self, nome_tecido, foto_tecido):
        self.nome_tecido = nome_tecido
        self.foto_tecido = foto_tecido
        
    def retorna_nome_tecido(self): #função pra identificar o tecido pelo nome ou palavras chave
        return self.nome_tecido

class Pedido:

    # Deve conter informações sobre o cliente e sobre
    # as máscaras que ele solicitou, tais como:
    # Cliente, prazo de entrega(se previamente definido,
    # caso contrário é indeterminado), valor total do pedido
    # e lista de máscaras solicitadas

    def __init__(self):
        pass
    
    def criar_pedido(self, cliente): #pra cada máscara existe um tecido e um tamanho que podem
                                     #variar de acordo com cada pedido.
                                     #TODO: como fazer para a cada máscara diferente poder inserir o tamanho e o tecido?