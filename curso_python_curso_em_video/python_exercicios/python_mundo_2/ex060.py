# Ex060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número para calcular seu fatorial: 5
# Calculando 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {num}! = ',end='')
fatorial = 1
while num != 1:
    print(f'{num}', end='')
    print(' x ' if num != 1 else ' = ', end='')
    fatorial *= num
    num -= 1
    if num == 1:
        print(f'1 = {fatorial}')