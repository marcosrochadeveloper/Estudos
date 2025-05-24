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

from time import sleep
from random import randint
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
if jogada == 0:
    jogadatxt = 'PEDRA'
elif jogada == 1:
    jogadatxt = 'PAPEL'
elif jogada == 2:
    jogadatxt = 'TESOURA'
else:
    print('X-X-X JOGADA INVÁLIDA X-X-X')
jogadapc = randint(0,2)
if jogadapc == 0:
    jogadapctxt = 'PEDRA'
elif jogadapc == 1:
    jogadapctxt = 'PAPEL'
elif jogadapc == 2:
    jogadapctxt = 'TESOURA'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-='*13)
print(f'{f'Computador jogou {jogadapctxt}':^26}')
print(f'{f'Jogador jogou {jogadatxt}':^26}')
print('-='*13)
if jogada == jogadapc:
    print('EMPATE!!!')
elif jogada == 0 and jogadapc == 1 or jogada == 1 and jogadapc == 2 or jogada == 2 and jogadapc == 0:
    print('Computador GANHOU!!!')
elif jogada == 0 and jogadapc == 2 or jogada == 1 and jogadapc == 0 or jogada == 2 and jogadapc == 1:
    print('Jogador GANHOU!!!')