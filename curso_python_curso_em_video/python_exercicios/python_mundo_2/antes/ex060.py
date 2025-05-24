# Ex060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número para calcular seu fatorial: 5
# Calculando 5! = 5 x 4 x 3 x 2 x 1 = 120

fatorial = int(input('Digite um número para calcular seu fatorial: '))
c = fatorial
totalfatorial = fatorial
print(f'Calculando {fatorial}! = {fatorial}',end='')
while c != 1:
    print(f' x {c-1}',end='')
    c -= 1
    totalfatorial = totalfatorial * c
print(f' = {totalfatorial}')