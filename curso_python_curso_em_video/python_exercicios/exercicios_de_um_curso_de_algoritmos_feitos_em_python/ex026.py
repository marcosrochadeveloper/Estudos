#26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo:
#- O primeiro valor é o maior
#- O segundo valor é o maior
#- Não existe valor maior, os dois são iguais

try:
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outro número inteiro: '))
    if num1 > num2:
        print('O primeiro valor é maior.')
    elif num2 > num1:
        print('O segundo valor é maior.')
    else:
        print('Não existe valor maior, os dois são iguais!')
except ValueError:
    print('Entrada Inválida! Por favor, digite um número inteiro válido.')