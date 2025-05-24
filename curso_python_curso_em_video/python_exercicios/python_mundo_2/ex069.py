# Ex069 - Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ------------------------------
#      CADASTRE UMA PESSOA
# ------------------------------
# Idade: 15
# Sexo: [M/F] m
# ------------------------------
# Quer continuar? [S/N] s
# ------------------------------
#      CADASTRE UMA PESSOA
# ------------------------------
# Idade: 10
# Sexo: [M/F] f
# ------------------------------
# Quer continuar? [S/N] s
# ------------------------------
#      CADASTRE UMA PESSOA
# ------------------------------
# Idade: 25
# Sexo: [M/F] m
# ------------------------------
# Quer continuar? [S/N] n
# Tivemos um total de 1 pessoas cadastradas com mais de 18 anos
# No total temos 2 homens cadastrados
# E temos 1 mulheres com menos de 20 anos
maior18 = homens = menos20 = 0
while True:
    print('-' * 30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper().strip()[0])
    while sexo not in 'MF':
        sexo = str(input('Dados Inválidos! Informe um Sexo [M/F]: ').upper().strip()[0])
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        menos20 += 1
    continuar = str(input('Quer continuar? [S/N]: ').upper().strip()[0])
    while continuar not in 'SN':
        continuar = str(input('Dados Inválidos! Quer continuar? [S/N]: ').upper().strip()[0])
    if continuar == 'N':
        break
print(f'''A) Tivemos um total de {maior18} pessoas cadastradas com mais de 18 anos
B) No total temos {homens} homens cadastrados
C) E temos {menos20} mulheres com menos de 20 anos''')
