# Ex072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from random import randint
extensos = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = randint(0,20)
# num = int(input('Digite um número entre 0 e 20: '))
# while num > 20 or num < 0:
#     num = int(input('Inválido! Informe um número entre 0 e 20: '))
# print(extensos[num])
print(f'Sorteado número {extensos[num]}')