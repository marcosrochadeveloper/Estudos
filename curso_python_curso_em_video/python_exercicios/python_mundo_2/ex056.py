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
# a) A média de idade do grupo é de 23.2 anos
# b) O homem mais velho tem 35 anos e se chama João
# c) No total são 1 mulheres com menos de 20 anos
total = maisvelho = mulheres20 = 0
for c in range(1,5):
    print(f'{f' {c}ª Pessoa ':-^21}')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())
    total += idade
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
media = total / 4
print(f'''A média de idade do grupo é de {media:.1f} anos
O homem mais velho tem {maisvelho} anos e se chama {nomemaisvelho}
Ao todo são {mulheres20} mulheres com menos de 20 anos''')