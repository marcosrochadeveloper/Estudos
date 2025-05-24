# Ex084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
resposta = 'S'
pessoas = []
dados = []
total_pessoas = maior_peso = menor_peso = 0
nomes_maior_peso = []
nomes_menor_peso = []

while resposta != 'N':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    total_pessoas += 1
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('Resposta Inválida! Quer continuar? [S/N]: ').strip().upper()[0])

for e, p in enumerate(pessoas):
    if p[1] > maior_peso: #p[1] == Peso
        maior_peso = p[1]
    if e == 0 or p[1] < menor_peso:
        menor_peso = p[1]

for p in pessoas:
    if p[1] == maior_peso:
        nomes_maior_peso.append(p[0])
    if p[1] == menor_peso:
        nomes_menor_peso.append(p[0])

print('-='*30)
print(f'A) Ao todo, você cadastrou {total_pessoas} pessoas.')
print(f'B) O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for nome in nomes_maior_peso:
    print(f'[{nome}]', end=' ')
print(f'\nC) O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for nome in nomes_menor_peso:
    print(f'[{nome}]', end=' ')