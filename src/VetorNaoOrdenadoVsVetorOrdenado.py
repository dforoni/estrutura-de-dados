# Vetor não ordenado

import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=float)

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
    else:
      self.ultima_posicao += 1 
      self.valores[self.ultima_posicao] = valor 

  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1

  # O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]
      
      self.ultima_posicao -= 1


# Vetor ordenado

class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=float)

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade atingida')
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

  def pesquisa_linear(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i
  
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao
    
    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      if self.valores[posicao_atual] == valor:
        return posicao_atual              
      elif limite_inferior > limite_superior:
        return -1
      else:
        if self.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual + 1
        else:
          limite_superior = posicao_atual - 1;

  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]
      
      self.ultima_posicao -= 1

# Inserção - Teste

import random

round(random.random(), 4)

elementos = []
for _ in range(10000):
  elementos.append(round(random.random(), 4))

len(elementos)

def insere_nao_ordenado(lista):
  vetor = VetorNaoOrdenado(len(lista))
  for i in lista:
    vetor.insere(i)
  return vetor

%timeit insere_nao_ordenado(elementos)

def insere_ordenado(lista):
  vetor = VetorOrdenado(len(lista))
  for i in lista:
    vetor.insere(i)
  return vetor

%timeit insere_ordenado(elementos)

# Pesquisa

vetor_nao_ordenado = insere_nao_ordenado(elementos)

len(vetor_nao_ordenado.valores)

vetor_ordenado = insere_ordenado(elementos)
len(vetor_nao_ordenado.valores)

pesquisa = []
for _ in range(10000):
  pesquisa.append(round(random.random(), 4))
len(pesquisa)

def pesquisa_nao_ordenado(lista):
  for i in lista:
    vetor_nao_ordenado.pesquisar(i)

%timeit pesquisa_nao_ordenado(pesquisa)

def pesquisa_ordenado_binaria(lista):
  for i in lista:
    vetor_ordenado.pesquisa_binaria(i)

%timeit pesquisa_ordenado_binaria(pesquisa)
