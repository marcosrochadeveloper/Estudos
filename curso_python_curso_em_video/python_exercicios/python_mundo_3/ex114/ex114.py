# Ex114 - Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from urllib import request
try:
    url = request.urlopen('https://www.pudim.com.br/')
except:
    print('\033[31mO site Pudim não está acessível no momento!\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')


# import requests
# try:
#     url = str(requests.get('https://www.pudim.com.br/'))
#     print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
# except:
#     print('\033[31mO site Pudim não está acessível no momento!\033[m')