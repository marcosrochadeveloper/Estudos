# 60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

mais30 = menos18 = c = mais_velha = mais_jovem = total_idades = total_pessoas = 0
nome_mais_jovem = nome_mais_velha = 0
try:
    while True:
        nome = str(input(f'Informe o nome da {c+1}ª pessoa: '))
        idade = int(input(f'Informe a idade da {c+1}ª pessoa: '))
        sexo = str(input(f'Informe o sexo da {c+1}ª pessoa: ').upper())
        c += 1
        total_idades += idade
        if mais_velha == 0 or mais_velha < idade:
            mais_velha = idade
            nome_mais_velha = nome
        if sexo == 'F' and (mais_jovem == 0 or idade < mais_jovem):
            mais_jovem = idade
            nome_mais_jovem = nome
        if sexo == 'M' and idade > 30:
            mais30 += 1
        if sexo == 'F' and idade < 18:
            menos18 += 1
        continuar = str(input('Quer continuar?[S/N] ').upper())
        if continuar == 'N':
            break
except ValueError:
    print('Entrada inválida! Por favor informe valores válidos!')
print(f'''a) O nome da pessoa mais velha é {nome_mais_velha}
b) O nome da mulher mais jovem é {nome_mais_jovem}
c) A média de idade do grupo é {total_idades / c}
d) {mais30} homens tem mais de 30 anos
e) {menos18} mulheres tem menos de 18 anos''')