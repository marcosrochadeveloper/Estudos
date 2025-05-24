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

mais18 = homens = menos20 = 0
while True:
    print('-'*30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper())
    print('-'*30)
    continuar = str(input('Quer continuar? [S/N] ').upper())
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    if continuar == 'N':
        break
print(f'Tivemos um total de {mais18} pessoas cadastradas com mais de 18 anos')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {menos20} mulheres com menos de 20 anos')