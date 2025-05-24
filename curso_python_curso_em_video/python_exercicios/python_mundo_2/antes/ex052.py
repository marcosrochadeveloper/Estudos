# Ex052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 11
# O número 11 foi divisível 2 vezes
# E por isso ele É PRIMO!

número = int(input('Digite um número: '))
divisão = 0
for c in range(1,número+1):
    if número%c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        divisão += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if divisão == 2:
    primo = '\033[32mÉ PRIMO!\033[m'
else:
    primo = '\033[31mNÃO É PRIMO!\033[m'
print(f'O número {número} foi divisível {divisão} vezes')
print(f'E por isso ele {primo}')