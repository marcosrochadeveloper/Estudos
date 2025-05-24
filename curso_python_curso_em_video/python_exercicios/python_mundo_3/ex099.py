# Ex099 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from time import sleep
def maior(* num):
    cont = num_maior = 0
    print('-='*40)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        if n > num_maior or cont == 0:
            num_maior = n
        sleep(0.2)
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {num_maior}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(-5,-4,-3,-2)