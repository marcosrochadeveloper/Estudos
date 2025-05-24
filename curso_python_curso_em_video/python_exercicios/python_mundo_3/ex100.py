# Ex100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from random import randint
from time import sleep

def sorteia(valor, quant):
    print(f'Sorteando {quant} valores da lista: ', end='')
    for c in range(quant):
        vl = randint(1,9)
        valor.append(vl)
        print(vl, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(valores):
    total_pares = 0
    for v in valores:
        if v%2 == 0:
            total_pares += v
    print(f'Somando os valores pares de {valores}, temos {total_pares}')


valores = list()
sorteia(valores, 5)
somaPar(valores)