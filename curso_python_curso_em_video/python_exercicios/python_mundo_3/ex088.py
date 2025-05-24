# Ex088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from random import randint, sample
from time import sleep

print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
jogo = []
cont = 0
for c in range(0, quantidade):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            cont = 0
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

print(f'-=-=-= SORTEANDO {quantidade} JOGOS -=-=-=')

for e, c in enumerate(jogos):
    print(f'Jogo {e+1}: {c}')
    sleep(0.5)

print('-=-=-=-= < BOA SORTE! > -=-=-=-=')