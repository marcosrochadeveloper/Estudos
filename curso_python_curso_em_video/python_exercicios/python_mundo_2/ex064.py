# Ex064 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número [999 para parar]: 1
# Digite um número [999 para parar]: 5
# Digite um número [999 para parar]: 10
# Digite um número [999 para parar]: 20
# Digite um número [999 para parar]: 35
# Digite um número [999 para parar]: 999
# Você digitou 5 números e a soma entre eles foi 71.

total = quantidade = num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        quantidade += 1
        total += num
print(f'Você digitou {quantidade} números e a soma entre eles foi {total}.')

# total = quantidade = num = 0
# num = int(input('Digite um número [999 para parar]: '))
# while num != 999:
#    quantidade += 1
#    total += num
#    num = int(input('Digite um número [999 para parar]: '))
# print(f'Você digitou {quantidade} números e a soma entre eles foi {total}.')