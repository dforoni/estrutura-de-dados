import numpy as np

# Classe No
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

# Classe Lista Encadeada

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None