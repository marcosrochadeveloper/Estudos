#49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.

numeros = []
c = pares = impares = 0
while c < 6:
    numero = int(input(f'Informe o {c+1}º número inteiro: '))
    numeros.append(numero)
    if numero%2 == 0:
        pares += 1
    else:
        impares += 1
    c += 1
print(f'Nos números {numeros} temos {pares} pares e {impares} ímpares!')