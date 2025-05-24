# Ex063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ------------------------------
# Sequência de Fibonacci
# ------------------------------
# Quantos termos você quer mostrar? 15
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 0 → 1 → 1 → 2 → 3 → 5 → 8 → 13 → 21 → 34 → 55 → 89 → 144 → 233 → 377 → FIM
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('-'*30)
print(f'{'Sequência de Fibonacci':^30}')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
c = 0
anterior = 0
atual = 0
proximo = 1
while c < n:
    print(atual, end = ' → ')
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    n -= 1
print('FIM')
print('~' * 30)