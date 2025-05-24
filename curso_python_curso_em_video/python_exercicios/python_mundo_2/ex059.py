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

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
option = 0
while option != 5:
    option = int(input(f'''{'=-='*10}
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
>>>>> Qual é a sua opção? '''))
    if option == 1:
        print(f'A soma entre {valor1} + {valor2} é {valor1+valor2}')
    elif option == 2:
        print(f'O resultado de {valor1} x {valor2} é {valor1*valor2}')
    elif option == 3:
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2} o maior é {valor1}')
        elif valor2 > valor1:
            print(f'Entre {valor1} e {valor2} o maior é {valor2}')
        else:
            print('Os valores são iguais!')
    elif option == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente!!!')
