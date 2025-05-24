#50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
#a) Quais foram os números sorteados
#b) Quantos números estão acima de 5
#c) Quantos números são divisíveis por 3

from random import randint
numeros = []
divide3 = acima = 0
while True:
    numeros.append(randint(0,10))
    if len(numeros) == 20:
        break
for numero in numeros:
    if numero > 5:
        acima += 1
    if numero%3 == 0:
        divide3 += 1
print(f'a) Foram sorteados os números {numeros}')
print(f'b) Foram sorteados {acima} números acima de 5!')
print(f'c) Foram sorteados {divide3} números divisíveis por 3!')