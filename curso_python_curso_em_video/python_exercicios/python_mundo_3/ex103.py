# Ex103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#

def ficha(nome = '', gols = ''):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    else:
        gols = int(gols)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

print('-'*30)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))

ficha(n, g)