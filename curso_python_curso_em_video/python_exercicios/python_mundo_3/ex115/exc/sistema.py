from time import sleep
def principal():
    while True:
        try:
            with open("cursoemvideo.txt", "x") as arquivo:
                print('Arquivo cursoemvideo.txt criado com sucesso!')
        except:
            break
    while True:
        print('-'*40)
        print('MENU PRINCIPAL'.center(40))
        print('-' * 40)
        print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
        print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
        print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
        print('-' * 40)
        while True:
            try:
                opcao = int(input('\033[33mSua Opção: \033[m'))
            except:
                print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            else:
                break

        if opcao > 0 and opcao < 4:
            if opcao == 1:
                op1()
            elif opcao == 2:
                op2()
            elif opcao == 3:
                op3()
                break
        else:
            print('\033[31mERRO: Digite uma opção válida!\033[m')
            sleep(1)


def op1():
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)
    sleep(1)
    with open('cursoemvideo.txt', 'r', encoding ='utf-8') as arquivo:
        pessoas = arquivo.readlines()
        for p in pessoas:
            p = p.strip() # A função
            print(f'{p[:-3]:<30}', end='')
            print(f'{p[-3:]} anos')


def op2():
    print('-' * 40)
    print('NOVO CADASTRO'.center(40))
    print('-' * 40)
    sleep(1)
    with open('cursoemvideo.txt', 'a', encoding ='utf-8') as arquivo:
        nome = str(input('Nome: '))
        while True:
            try:
                idade = int(input('Idade: '))
                break
            except:
                print('ERRO: Por favor, digite um número inteiro válido.')
        arquivo.write(f'{nome} {idade}\n')

def op3():
    print('-' * 40)
    print('Saindo do sistema... Até logo!'.center(40))
    print('-' * 40)