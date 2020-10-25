# Vetor não Ordenado

## Set up
import numpy as np

## Classe vetor não ordenado

class VetorNaoOrdenado:
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

    # Inserção - O(1) é uma função constante, pois sempre executará o mesmo número de passo
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1 # como no python o index começa no zero, qdo incrementar 1 o index será zero
            self.valores[self.ultima_posicao] = valor

    # Pesquisa Linear - O(n) conforme o valor da entrada, será o número de passos da função (linearmente)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
          if valor == self.valores[i]:
            return i
        return -1
    
    # Exclusão
    
## Teste Vetor Vazio

vetor = VetorNaoOrdenado(4)
vetor.imprime()

## Teste Inserção
vetor.insere(2)
vetor.imprime()

vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()

## Teste Pesquisar

vetor.pesquisar(2)
