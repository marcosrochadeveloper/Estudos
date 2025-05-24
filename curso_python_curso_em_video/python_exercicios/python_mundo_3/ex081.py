# Ex081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
numeros = []
resposta = 'S'
total = 0
while resposta != 'N':
    numeros.append(int(input('Digite um valor: ')))
    total += 1
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Resposta Inválida! Quer continuar? [S/N]: ').strip().upper()[0])
numeros.sort(reverse=True)
print(f'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
A) Você digitou {total} números.
B) Os valores em ordem decrescente são {numeros}
C) O valor 5 {'faz parte da lista!' if 5 in numeros else 'não foi encontrado na lista!'}''')
