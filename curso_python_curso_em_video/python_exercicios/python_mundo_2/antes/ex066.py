# Ex066 - Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um valor (999 para parar): 5
# Digite um valor (999 para parar): 10
# Digite um valor (999 para parar): 25
# Digite um valor (999 para parar): 35
# Digite um valor (999 para parar): 951
# Digite um valor (999 para parar): 999
# A soma dos 5 valores foi 1026!

quantidade = 0
total = 0
while True:
    número = int(input('Digite um valor (999 para parar): '))
    if número != 999:
        quantidade += 1
        total += número
    else:
        break
print(f'A soma dos {quantidade} valores foi {total}!')