# Ex091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1': randint(1,6), 'Jogador2': randint(1,6), 'Jogador3': randint(1,6), 'Jogador4': randint(1,6)}

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('Valores sorteados:')
sleep(0.5)

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

print('-='*30)
print(f'{'  == RANKING DOS JOGADORES ==':^31}')

for e, v in enumerate(ranking):
    print(f'{f'   {e+1}º lugar: {v[0]} com {v[1]}':^30}')
    sleep(0.5)
