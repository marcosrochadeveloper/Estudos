# Ex082 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
numeros = []
pares = []
impares = []
resposta = 'S'
while resposta != 'N':
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Resposta Inválida! Quer continuar? [S/N]: ').strip().upper()[0])
print(f'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
A lista completa é {numeros}
A lista de pares é {pares}
A lista de ímpares é {impares}''')