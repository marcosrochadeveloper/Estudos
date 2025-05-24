# Ex085 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
numeros = [[],[]]
for c in range(1,8):
    numero = int(input(f'Informe o {c}º número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(f'Números pares: {sorted(numeros[0])}')
print(f'Números ímpares: {sorted(numeros[1])}')