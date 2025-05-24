# Ex094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
pessoas = []
resposta = 'S'
total_idades = 0
while resposta != 'N':
    pessoa = {'Nome': str(input('Nome: ')), 'Sexo': str(input('Sexo[M/F]: ').strip().upper()[0])}
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('ERRO! Por favor, digite apenas M ou F.\nSexo[M/F]: ').strip().upper()[0])
    pessoa['Idade'] = int(input('Idade: '))
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('ERRO! Por favor, digite apenas S ou N.\nQuer continuar? [S/N]: ').strip().upper()[0])
    pessoas.append(pessoa)

print('-='*30)
for p in pessoas:
    total_idades += p['Idade']
media = total_idades/len(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')

for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'[{p['Nome']}]', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')

for p in pessoas:
    if p['Idade'] > media:
        print(f'   Nome = {p['Nome']}; Sexo = {p['Sexo']}; Idade = {p['Idade']};')

print('<< ENCERRADO >>')
