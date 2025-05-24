# Ex045 - Crie um programa que faça o computador jogar Jokenpô com você.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA
# Qual é a sua jogada? 1
# JO
# KEN
# PO!!!
# -=-=-=-=-=-=-=-=-=-=-=
# Computador jogou PAPEL
# Jogador jogou PAPEL
# -=-=-=-=-=-=-=-=-=-=-=
# EMPATE!!!
from random import choice
from time import sleep
options = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = options[int(input('''[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA \nQual é a sua jogada? '''))]
computador = choice(options)

for i in ['JO', 'KEN', 'PO!!!']:
    print(i), sleep(0.5)

print(f'''{'-='*12}-
{f'Jogador jogou {jogador}':^25}
{f'Computador jogou {computador}':^25}                                                   
{'-='*12}-''')

ganho_computador = [['PEDRA', 'PAPEL'], ['PAPEL', 'TESOURA'], ['TESOURA','PEDRA']]

if jogador == computador:
    print('EMPATE')
elif [jogador, computador] in ganho_computador:
    print('COMPUTADOR GANHOU')
else:
    print('JOGADOR GANHOU')
