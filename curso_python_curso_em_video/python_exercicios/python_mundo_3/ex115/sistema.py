from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print(f'Arquivo {arq} criado com sucesso!')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Esvaziar Arquivo', 'Remover Cadastro', 'Sair do Sistema'])
    if resposta == 5:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        options(resposta)
    sleep(2)
