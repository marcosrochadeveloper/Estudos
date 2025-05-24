# Ex079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
resposta = 'S'
valores = []
while resposta != 'N':
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = int(input('Resposta inválida! Quer continuar? [S/N]: '))
valores.sort()
print('-='*20)
print(f'Você digitou os valores {valores}')