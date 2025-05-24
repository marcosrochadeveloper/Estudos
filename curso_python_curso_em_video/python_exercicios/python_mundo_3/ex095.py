# Ex095 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
time = []
resposta = 'S'
while resposta != 'N':
    jogador = {
        'Cod': len(time),
        'Nome': str(input('Nome do jogador: ')),
        'Gols': [],
        'Total': 0}
    partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    for c in range(0, partidas):
        jogador['Gols'].append(int(input(f'   Quantos gols na Partida {c}? ')))
        jogador['Total'] += jogador['Gols'][c]
    time.append(jogador.copy())
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Resposta Inválida! Quer continuar? [S/N]: ').strip().upper()[0])
print('-='*30)

for e, k in enumerate(jogador.keys()):
    if e == 0:
        print(f'{k:>3}', end=' ')
    elif e == 1:
        print(f'{k:<14}', end=' ')
    elif e == 2:
        print(f'{k:<14}', end=' ')
    elif e == 3:
        print(f'{k:<6}', end=' ')
print()
print('-'*40)
for j in time:
    for e, v in enumerate(j.values()):
        if e == 0:
            print(f'{v:>3}', end=' ')
        elif e == 1:
            print(f'{v:<14}', end=' ')
        elif e == 2:
            print(f'{str(v):<14}', end=' ')
        elif e == 3:
            print(f'{str(v):<6}', end=' ')
    print()
print('-'*40)
mostrar = 0
while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    while mostrar >= len(time) or mostrar < 0:
        print(f'ERRO! Não existe jogador com código {mostrar}!')
        print('-' * 40)
        mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if mostrar == 999:
            break
    if mostrar != 999:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[mostrar]['Nome']}:')
        for e, g in enumerate(time[mostrar]['Gols']):
            print(f'    => No jogo {e+1}, fez {g} gols.')
        print(f'     Foi um total de {time[mostrar]['Total']} gols.')
        print('-' * 40)
    else:
        break
print('<< VOLTE SEMPRE >>')