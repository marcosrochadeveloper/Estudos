# Ex065 - Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 3
# Quer continuar? [S/N] s
# Digite um número: 25
# Quer continuar? [S/N] s
# Digite um número: 958
# Quer continuar? [S/N] s
# Digite um número: 2
# Quer continuar? [S/N] n
# Você digitou 4 números e a média foi 247.0
# O maior valor foi 958 e o menor foi 2
continuar = 'S'
maior = menor = quantidade = total = 0
while continuar != 'N':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]: ').upper().strip()[0])
    while continuar not in 'SN':
        continuar = str(input('Entrada Inválida! Quer continuar? [S/N]: ').upper().strip()[0])
    quantidade += 1
    total += num
    if num > maior:
        maior = num
    if menor == 0 or num < menor:
        menor = num

print(f'''Você digitou {quantidade} números e a média foi {total/quantidade:.1f}
O maior valor foi {maior} e o menor foi {menor}''')
