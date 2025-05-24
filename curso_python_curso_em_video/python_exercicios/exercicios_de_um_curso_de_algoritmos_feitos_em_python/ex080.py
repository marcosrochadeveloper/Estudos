# 80) Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e 15 sorteados pelo computador.
# Depois disso, peça para o usuário digitar um número (chave) e seu programa deve mostrar em que posições essa chave foi encontrada.
# Mostre também quantas vezes a chave foi sorteada.

from random import randint
vetor = []
vezes_sorteado = 0
count = 0
posicoes= []
for c in range(30):
    vetor.append(randint(1,15))
num = int(input('Escolha um número entre 1 e 15: '))
for n in vetor:
    if n == num:
        vezes_sorteado += 1
        posicoes.append(count)
        count += 1
print(vetor)
print(f'esse número foi encontrado nas posições {posicoes} e foi sorteado {vezes_sorteado} vezes')