from ..arquivo import *

def leiaInt(n):
    while True:
        try:
            num = int(input(n).strip())
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m ')
        except KeyboardInterrupt:
            print('\033[31m\nEntrada de dados interrompida pelo usuário.\033[m ')
        else:
            return num


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    while True:
        opc = leiaInt('\033[33mSua Opção: \033[m')
        if opc < 1 or opc > 5:
            print('\033[31mOPÇÃO INVÁLIDA! Informe uma opção entre 1 e 4!!!\033[m')
            continue
        else:
            break
    return opc


def principal():
    print()


def options(opc):
    if opc == 1:
        lerArquivo()
    elif opc == 2:
        cadastrar()
    elif opc == 3:
        limparArquivo()
    elif opc == 4:
        removerCadastro()