# 62) Faça um programa usando a estrutura “faça enquanto” que leia a idade de
# várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
# não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

total_idades = soma_idades = mais21 = 0
while True:
    idade = int(input('Informe uma idade: '))
    total_idades += 1
    soma_idades += idade
    if idade >= 21:
        mais21 += 1
    continuar = str(input('Quer continuar [S/N]? ').upper())
    if continuar == 'N':
        break
print(f'''a) Foram digitadas {total_idades} idades.
b) A média das idades digitadas foi de aproximadamente {int(soma_idades/total_idades)}
c) {mais21} pessoas tem 21 anos ou mais.''')