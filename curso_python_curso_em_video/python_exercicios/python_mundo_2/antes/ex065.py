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

resposta = ''
total = 0
soma = 0
números = []
c = 0
while resposta != 'N':
    número = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    total += 1
    soma += número
    números.append(número)
maior = números[0]
menor = números[0]
while c < len(números):
    if números[c] > maior:
        maior = números[c]
    if números[c] < menor:
        menor = números[c]
    c += 1
média = soma/total
print(f'Você digitou {total} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')