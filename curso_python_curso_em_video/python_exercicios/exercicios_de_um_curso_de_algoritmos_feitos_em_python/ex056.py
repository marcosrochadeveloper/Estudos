# 56) Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
# Obs: O programa será interrompido quando o número 1111 for digitado

numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero == 1111:
        break
    numeros.append(numero)
soma = 0
for n in numeros:
    soma += n

print(f'A soma dos números digitados é igual a {soma}!')