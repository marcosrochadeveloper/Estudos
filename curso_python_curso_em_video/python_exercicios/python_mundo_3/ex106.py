# Ex106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from time import sleep

c = ('\033[m',             # 0 - Sem Cores
     '\033[0;41m',  # 1 - Vermelho
     '\033[0;42m',  # 2 - Verde
     '\033[0;43m',  # 3 - Amarelo
     '\033[0;44m',  # 4 - Azul
     '\033[0;45m',  # 5 - Roxo
     '\033[0;46m',  # 6 - Azul Tiffany
     '\033[0;47m',  # 7 - Cinza
     '\033[07;40m', # 8 - Branco
    )

def ajuda(com):
    titulo(f' Acessando o manual do comando \'{com}\'', 4)
    print(c[8],end='')
    help(com)
    print(c[0],end='')
    sleep(1)


def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    print('\033[42m~'*25)
    print('\033[42m SISTEMA DE AJUDA PyHELP')
    print('\033[42m~'*25)
    comando = str(input('\033[mFunção ou Biblioteca > ').lower())
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)