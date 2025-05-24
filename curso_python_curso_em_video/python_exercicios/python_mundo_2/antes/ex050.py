# Ex050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite o 1º valor: 1
# Digite o 2º valor: 2
# Digite o 3º valor: 3
# Digite o 4º valor: 4
# Digite o 5º valor: 5
# Digite o 6º valor: 6
# Foram informados 3 números PARES, somando todos eles temos o valor 12

soma = 0
total = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero %2 == 0:
        soma += numero
        total += 1
print(f'Foram informados {total} números PARES, somando todos eles temos o valor {soma}')