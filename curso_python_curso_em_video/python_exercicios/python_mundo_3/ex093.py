# Ex093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
jogador = {
    'Nome': str(input('Nome do jogador: ')),
    'Gols': [],
    'Total': 0}
partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for c in range(0, partidas):
    jogador['Gols'].append(int(input(f'   Quantos gols na Partida {c}? ')))
    jogador['Total'] += jogador['Gols'][c]
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.')
for e, g in enumerate(jogador['Gols']):
    print(f'    => Na partida {e}, fez {g} gols.')
print(f'Foi um total de {jogador['Total']} gols.')