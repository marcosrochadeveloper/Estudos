# 76) Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo
# computador e depois mostre os valores gerados na tela.

from random import randint
vetor = []
for c in range(7):
    vetor.append(randint(0,10))
print(vetor)