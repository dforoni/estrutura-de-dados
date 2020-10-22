## Notação Big-O
'''
- Como comparar algoritmos?
- Comparação objetiva entre algoritmos.
- Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação.
- O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas.

'''

### Função 1 - O(n)

def soma(n):
    soma = 0
    
    for i in range(n + 1):
        soma += i
    return soma

s = soma(10)
print(s)