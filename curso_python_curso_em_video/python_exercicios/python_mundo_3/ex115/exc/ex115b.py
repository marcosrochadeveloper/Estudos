# Ex115b - Vamos ver como fazer acesso a arquivos usando o Python.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from sistema import *
while True:
    try:
        open("cursoemvideo.txt", "x")
        print('Arquivo cursoemvideo.txt criado com sucesso!')
    except:
        break

arquivo = open("cursoemvideo.txt", "r")


principal(arquivo)