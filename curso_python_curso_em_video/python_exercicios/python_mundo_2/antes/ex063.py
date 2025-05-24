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
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
print('0 →',end='')
c = 0
anterior = 0
atual = 1
próximo = anterior+atual
while c <= termos-2:
    print(f' {atual} →',end='')
    anterior = atual
    atual = próximo
    próximo = anterior+atual
    c += 1
print(' FIM')
print('~'*30)