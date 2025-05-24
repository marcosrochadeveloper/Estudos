# Ex056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a) A média de idade do grupo
# b) Qual é o nome do homem mais velho
# c) Quantas mulheres têm menos de 20 anos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ----- 1ª Pessoa -----
# Nome: João
# Idade: 35
# Sexo [M/F]: m
# ----- 2ª Pessoa -----
# Nome: Pedro
# Idade: 20
# Sexo [M/F]: m
# ----- 3ª Pessoa -----
# Nome: Joana
# Idade: 18
# Sexo [M/F]: f
# ----- 4ª Pessoa -----
# Nome: Bianca
# Idade: 20
# Sexo [M/F]: f
# a) A média de idade do grupo é de 23.25 anos
# b) O homem mais velho tem 35 anos e se chama João
# c) No total são 1 mulheres com menos de 20 anos

nomes = []
idades = []
sexos = []
idademaisvelho = 0
nomemaisvelho = ''
mulheresmenores = 0
for c in range(1,5):
    print(f'----- {c}ª Pessoa -----')
    nomes.append(str(input('Nome: ')))
    idades.append(int(input('Idade: ')))
    sexos.append(str(input('Sexo [M/F]: ').upper()))
média = (idades[0] + idades[1] + idades[2] + idades[3])/4
for c in range(0,4):
    if sexos[c] == 'M' and idades[c] > idademaisvelho:
        idademaisvelho = idades[c]
        nomemaisvelho = nomes[c]
    if sexos[c] == 'F' and idades[c] < 20:
        mulheresmenores += 1
print(f'a) A média de idade do grupo é de {média} anos')
print(f'b) O homem mais velho tem {idademaisvelho} anos e se chama {nomemaisvelho}')
print(f'c) No total são {mulheresmenores} mulheres com menos de 20 anos')