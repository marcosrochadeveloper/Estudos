# 59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
# perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens
contagem = maior = homens = mulher = soma_idade = 0
while True:
    sexo = str(input(f'Informe o sexo da {contagem+1}ª pessoa [M/F]: ').upper())
    idade = int(input(f'Informe a idade da {contagem+1}ª pessoa: '))
    if maior == 0:
        maior = idade
    elif maior < idade:
        maior = idade
    if sexo == 'M':
        homens += 1
        soma_idade += idade
    if sexo == 'F' and mulher == 0:
        mulher = idade
    elif sexo == 'F' and mulher > idade:
        mulher = idade
    contagem += 1
    continuar = str(input('Quer continuar? [S/N]').upper())
    if continuar == 'N':
        break

print(f'''a) A maior idade lida foi de {maior} anos!
b) Foram cadastrados {homens} homens!
c) A mulher mais jovem cadastrada tem {mulher} anos!
d) A média de idade entre os homens cadastrados é de aproximadamente {int(soma_idade/homens)} anos!''')