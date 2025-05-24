# Ex052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 11
# O número 11 foi divisível 2 vezes
# E por isso ele É PRIMO!

numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero+1):
    if numero%c == 0:
        print(f'\033[33m{c}\033[m',end=' ')
        total += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {numero} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')