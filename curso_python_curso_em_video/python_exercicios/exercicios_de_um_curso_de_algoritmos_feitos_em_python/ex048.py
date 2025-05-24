#48) Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.

numeros = []
c = 1
total = 0
while c < 8:
    numeros.append(int(input(f'Informe o {c}º número inteiro: ')))
    total += numeros[c-1]
    c+=1
print(f'A soma entre os números {numeros} é igual a {total}')