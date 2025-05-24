# 83) [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números aleatórios (entre 0 e 99) gerados pelo computador.
# Logo em seguida, mostre os números gerados e depois coloque o vetor em ordem crescente, mostrando no final os valores ordenados.

from random import randint
numeros = []
for c in range(20):
    numeros.append(randint(0,99))
print(numeros)
numeros.sort()
print(numeros)