# 54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

pesos = []
alturas = []
altura_total = mais90 = menos50menos160 = mais190mais100 = 0

for c in range(1,8):
    pesos.append(float(input(f'Informe o peso da {c}ª pessoa[Kg]: ')))
    alturas.append(float(input(f'Informe a altura da {c}ª pessoa[Em metros]: ')))
    altura_total += alturas[c-1]
    if pesos[c-1] > 90:
        mais90 += 1
    if pesos[c-1] < 50 and alturas[c-1] < 1.6:
        menos50menos160 += 1
    if pesos[c-1] > 100 and alturas[c-1] > 1.9:
        mais190mais100 += 1

print(f'a) A média de altura do grupo foi de {altura_total/7:.2f}')
print(f'b) {mais90} pessoas pesam mais de 90Kg!')
print(f'c) {menos50menos160} pessoas pesam menos de 50Kg e tem menos de 1.60m')
print(f'd) {mais190mais100} pessoas medem mais de 1.90m e pesam mais de 100Kg')