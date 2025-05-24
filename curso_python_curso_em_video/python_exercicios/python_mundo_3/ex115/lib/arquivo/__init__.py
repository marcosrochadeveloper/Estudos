from .. import interface
from time import sleep

def arquivoExiste(arq):
    try:
        with open(arq, "x") as arquivo:
            return True
    except:
        return False


def criarLista():
    with open('cursoemvideo.txt', 'r', encoding='utf-8') as arquivo:
        pessoas = arquivo.readlines()
        lista = []
        for p in pessoas:
            lista.append(p)
        return lista


def lerArquivo():
    try:
        with open('cursoemvideo.txt', 'r', encoding='utf-8') as arquivo:
            pessoas = arquivo.readlines()
            interface.cabecalho('PESSOAS CADASTRADAS')
            for e, p in enumerate(pessoas):
                p = p.strip()
                p = p.split(';')
                print(f'{e+1:<2} - {p[0]:<25} {p[1]:>3} anos')
                #print(f'{e+1:<2} - {p[:-3]:<25} {p[-2:]} anos')
    except:
        print('ERRO AO LER O ARQUIVO!')


def limparArquivo():
    resposta = str(input('Tem certeza que deseja esvaziar todo o arquivo de texto? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Resposta Inválida! Quer continuar? [S/N]: ').strip().upper()[0])
    if resposta == 'S':
        try:
            with open('cursoemvideo.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write('')
                interface.cabecalho('ARQUIVO LIMPO COM SUCESSO')
        except:
            print('HOUVE UM ERRO NA LIMPEZA DO ARQUIVO!')
    else:
        print('NÃO FORAM FEITAS ALTERAÇÕES NO ARQUIVO DE TEXTO, VOLTANDO AO MENU PRINCIPAL...')
        sleep(1)


def cadastrar():
    try:
        interface.cabecalho('CADASTRAR')
        with open('cursoemvideo.txt', 'a', encoding='utf-8') as arquivo:
            nome = str(input('Nome: '))
            idade = interface.leiaInt('Idade: ')
            arquivo.write(f'{nome};{idade}\n')
            print(f'\033[32mNovo registro de {nome} adicionado!\033[m')
    except:
        print('HOUVE UM ERRO NA ABERTURA DO ARQUIVO!')


def removerCadastro():
    lerArquivo()
    pessoas = criarLista()
    print(interface.linha())
    remover = interface.leiaInt('Escolha um número para remover seu cadastro: ')
    pessoa = pessoas[remover-1].split(';')
    print(f'Removendo cadastro de \033[33m{pessoa[0]}\033[m')
    pessoas.pop(remover-1)
    try:
        with open('cursoemvideo.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('')
    except:
        print('HOUVE UM ERRO NA LIMPEZA DO ARQUIVO!')
    with open('cursoemvideo.txt', 'a', encoding='utf-8') as arquivo:
        for p in pessoas:
            arquivo.write(f'{p}')