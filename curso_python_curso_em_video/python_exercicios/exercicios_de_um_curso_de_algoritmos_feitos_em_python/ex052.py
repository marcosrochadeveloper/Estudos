# 52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

idades = []
menos5 = mais18 = maior = soma = 0
for c in range(1,11):
    idades.append(int(input(f'Informe a {c}ª idade: ')))
    soma += idades[c-1]
    if idades[c-1] > 18:
        mais18 += 1
    if idades[c-1] < 5:
        menos5 += 1
    if idades[c-1] > maior:
        maior = idades[c-1]
print(f'a) A média de idade do grupo é de aproximadamente {int(soma/10)} anos!')
print(f'b) {mais18} pessoas nesse grupo tem mais de 18 anos!')
print(f'c) {menos5} pessoas nesse grupo tem menos de 5 anos!')
print(f'd) A maior idade lida foi {maior}')