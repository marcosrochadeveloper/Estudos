# Ex098 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from time import sleep
def contador (i, f, p):
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.3)
    else:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), abs(int(input('Passo: '))))