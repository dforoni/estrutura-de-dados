# Vetor Ordenado

## Set up
import numpy as np

## Classe vetor ordenado

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1 # -1 pois no python o index começa no zero
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    # Inserção - O(n) depende do número de elementos do vetor
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
            return
        
        posicao = 0

        for i in range(self.ultima_posicao + 1):
            posicao = i

            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
       
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # Pesquisar - O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1



## Teste Vetor Vazio

vetor = VetorOrdenado(8)
vetor.imprime()

## Teste Insere 

vetor.insere(4)
vetor.insere(6)
vetor.imprime()

## Teste Pesquuisa

vetor.pesquisar(6) 
