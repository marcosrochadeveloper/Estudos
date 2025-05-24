# 70) [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência de Fibonacci:
# 1 1 2 3 5 8 13 21...

anterior = 0
atual = 1
proximo = 1
for c in range(10):
    print(atual, end=' ')
    anterior = atual
    atual = proximo
    proximo = atual + anterior