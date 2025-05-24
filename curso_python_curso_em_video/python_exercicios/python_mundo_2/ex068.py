# Ex068 - Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# VAMOS JOGAR PAR OU ÍMPAR
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diga um valor (0 à 10): 5
# Par ou Ímpar? [P/I] p
# ------------------------------
# Você jogou 5 e o computador 1. Total de 6 DEU PAR
# ------------------------------
# Você VENCEU!
# Vamos jogar novamente...
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diga um valor (0 à 10): 2
# Par ou Ímpar? [P/I] i
# ------------------------------
# Você jogou 2 e o computador 6. Total de 8 DEU PAR
# ------------------------------
# Você PERDEU!
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# GAME OVER! Você venceu 1 vezes.
from random import randint
print(f'''{'=-'*15}
{'VAMOS JOGAR PAR OU ÍMPAR':^30}''')
vitorias = 0
while True:
    print('=-'*15)
    jogador = int(input('Diga um valor (0 à 10): '))
    computador = randint(0,10)
    total = jogador + computador
    resultado = 'PAR' if total%2 == 0 else 'ÍMPAR'
    parouimpar = str(input('Par ou Ímpar? [P/I]: ').upper().strip()[0])
    while parouimpar not in 'PI':
        parouimpar = str(input('Dados inválidos, quer escolher Par ou Ímpar? [P/I]: ').upper().strip()[0])
    tipo_jogador = 'PAR' if parouimpar == 'P' else 'ÍMPAR'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU {resultado}')
    print('-'*30)
    if resultado == tipo_jogador:
        print('Você VENCEU!\nVamos jogar novamente...')
        vitorias += 1
    else:
        print('Você perdeu!')
        print('=-' * 15)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')