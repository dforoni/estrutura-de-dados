import numpy as np

# Fila Circular

class FilaCircular:
    # Método
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    # Função Privada
    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila Cheia')
            return
        
        if self.final == self.capacidade -1:
          self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1
    
    def desenfileirar(self):
      if self.__fila_vazia():
          print('Fila Vazia')
          return
    
      temp = self.valores[self.inicio]
      self.inicio += 1
      if self.inicio == self.capacidade:
          self.inicio = 0
      self.numero_elementos -= 1
      return temp

    def primeiro(self):
      if self.__fila_vazia():
        return -1
      return self.valores[self.inicio]

# Teste 

fila = FilaCircular(5)

print(fila.primeiro())

# 1
fila.enfileirar(1)
print(fila.primeiro())

# 2 1
fila.enfileirar(2)
print(fila.primeiro())

# 5 4 3 2 1
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
print(fila.primeiro())

print(fila.enfileirar(6))

# 5 4 3
fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())     

# Fila 
print(fila.valores)

# Inicio e Final da Fila
print(fila.inicio, fila.final)