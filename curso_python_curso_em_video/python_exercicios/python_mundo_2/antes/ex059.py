# Ex059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro valor: 5
# Segundo valor: 5
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
# >>>>> Qual é a sua opção? 2
# O resultado de 5 x 5 é 25
# =-==-==-==-==-==-==-==-==-==-=
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
# >>>>> Qual é a sua opção? 5
# Finalizando...
# =-==-==-==-==-==-==-==-==-==-=

from time import sleep
opção = 0
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
while opção != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {valor1} + {valor2} é {valor1+valor2}')
        print('=-='*10)
        sleep(2)
    elif opção == 2:
        print(f'O resultado de {valor1} x {valor2} é {valor1*valor2}')
        print('=-=' * 10)
        sleep(2)
    elif opção == 3:
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2} o maior é {valor1}')
        elif valor2 > valor1:
            print(f'Entre {valor1} e {valor2} o maior é {valor2}')
        else:
            print('Os números são iguais!')
        print('=-=' * 10)
        sleep(2)
    elif opção == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        print('=-=' * 10)
        sleep(2)
    elif opção == 5:
        print('Finalizando...')
        print('=-=' * 10)
        sleep(2)
    else:
        print('Opção inválida! Tente Novamente')
        print('=-=' * 10)
        sleep(2)