#31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
from time import sleep
from random import randint

print('\033[33m---JoKenPo---\033[m')

opcao_jogador = int(input('''[1] Pedra
[2] Papel
[3] Tesoura
Escolha uma das opções acima: '''))

opcao_computador = randint(1,3)

if opcao_computador == 1:
    txtcomputador = 'Pedra'
elif opcao_computador == 2:
    txtcomputador = 'Papel'
elif opcao_computador == 3:
    txtcomputador = 'Tesoura'

if opcao_jogador == 1:
    txtjogador = 'Pedra'
elif opcao_jogador == 2:
    txtjogador = 'Papel'
elif opcao_jogador == 3:
    txtjogador = 'Tesoura'
else:
    print('Jogada Inválida!!')

if opcao_jogador == 1 or opcao_jogador == 2 or opcao_jogador == 3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print(f'Computador jogou {txtcomputador} e jogador jogou {txtjogador}!')
    if opcao_jogador == 1 and opcao_computador == 2 or opcao_jogador == 2 and opcao_computador == 3 or opcao_jogador == 3 and opcao_computador == 1:
        print('Computador Ganhou!')
    elif opcao_jogador == 1 and opcao_computador == 3 or opcao_jogador == 2  and opcao_computador == 1 or opcao_jogador == 3 and opcao_computador == 2:
        print('Jogador Ganhou!')
    else:
        print('EMPATE!')
else:
    print('Encerrando...')