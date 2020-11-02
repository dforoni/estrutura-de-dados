import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade # os '__' são para deixar privados estes valores, por medida de segurança, só tem acesso dentro da classe
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __cheia_pilha(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == self.__capacidade -1:
            return True
        else: 
            return False
    
    def empilhar(self, valor):
        if self.__cheia_pilha():
            print('Pilha Cheia!')
            return True
        else:
            self.__topo += 1
            self.__valores[self.__topo] == valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia!')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


# Teste - Classe

pilha = Pilha(5)
print(pilha)

# Teste - Topo
print(pilha.ver_topo())

# Teste - Empilhar

pilha.empilhar(1)
print(pilha.ver_topo())
