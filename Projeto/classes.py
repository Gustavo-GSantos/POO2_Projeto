#Primeiras classes e métodos identificados
from Tecidos import tecidos

class Cliente:

    # Deve conter informações que identifiquem o cliente
    # Nome, telefone, endereço(pra entrega)

    def __init__(self, nome_cliente, telefone_cliente, endereco_cliente):
        self.nome_cliente = nome_cliente
        self.telefone_cliente = telefone_cliente
        self.endereco_cliente = endereco_cliente
        
    
    def retorna_nome_cliente(self): #função para usar o nome do cliente no pedido
        return self.nome_cliente
        #pra ter uma rápida noção de quem é
        
    def retorna_info_cliente(self):
        return self.nome_cliente, self.telefone_cliente, self.endereco_cliente
        #TODO: Como retornar todas as informações do cliente? É possível ou melhor 3 métodos diferentes?

        #O objetivo de retornar todas as informações de uma vez é pra mostrar
        #a informação completa e saber exatamente quem é o cliente

class Mascara: #TODO: Mudar nome pra class Tecido? Já que os primeiros métodos são mais focados nisso
               #TODO: e considerando que as máscaras tem outros atributos como preço e tamanho

    # Deve conter informações sobre as máscaras
    # Valores serão fixos (tipo1 = 5 reais, tipo2 = 10 reais)

    def __init__(self, ID:int, tecido, tipo, tamanho:str):
        self.ID = ID
        self.tecido = tecido
        self.tipo = tipo
        if tipo == 'tipo1':
            vtipo = 5
        else:
            vtipo = 10
        self.valor = vtipo
        self.tamanho = tamanho
    
    def retorna_informações_mascara(self):
        return self.ID, self.tecido, self.tipo, self.valor, self.tamanho


class Pedido:

    # Deve conter informações sobre o cliente e sobre
    # as máscaras que ele solicitou, tais como:
    # Cliente, prazo de entrega(se previamente definido,
    # caso contrário é indeterminado), valor total do pedido
    # e lista de máscaras solicitadas

    def __init__(self, cliente, mascaras=[]):   #pra cada máscara existe um tecido e um tamanho que podem
        self.cliente = cliente                  #variar de acordo com cada pedido.
        self.mascaras = mascaras
        self.__vtotal = 0 # Atributo privado.
        for mascara in mascaras:                    
            self.__vtotal += mascara.valor          
        self.__valor_total = self.__vtotal # Atributo privado sem metodo setter para não haver mudanças fora da instanciação.
    
    @property                       # 
    def valor_total(self):          # Essa parte serve para retornar o valor privado
        return self.__valor_total   #


cliente1 = Cliente('Marcos', 123, 'Rua 123') #Instancia o cliente
cliente2 = Cliente('Maria', 321, 'Rua 321')

print(cliente1.retorna_info_cliente()) #Imprime todas as informações do Cliente

l = cliente2.retorna_info_cliente()
print(l[0]) #Imprime o nome
print(l[1]) #Imprime o telefone

mascara1 = Mascara(1, tecidos.tecido1, 'tipo1', 'Pequeno')
mascara2 = Mascara(2, tecidos.tecido2, 'tipo2', 'Medio')

t = mascara1.retorna_informações_mascara()
print(t[1])
print(t)

pedido1 = Pedido(cliente1, [Mascara(3, tecidos.tecido3, 'tipo2', 'Medio'), Mascara(4, tecidos.tecido1, 'tipo1', 'Pequeno')])
pedido2 = Pedido(cliente2, [mascara1, mascara2, mascara2, mascara2, mascara1])
print(f'Pedido 1: {pedido1.valor_total}')
print(f'Pedido 2: {pedido2.valor_total}')
