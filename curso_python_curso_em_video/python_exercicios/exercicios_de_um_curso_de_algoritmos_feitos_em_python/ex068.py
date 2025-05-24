# 68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens
total_mulheres = homens_mais100 = maior_peso = total_peso_mulheres = 0
for c in range(1,9):
    sexo = str(input(f'Informe o sexo da {c}ª pessoa [F/M]: ').upper())
    peso = float(input(f'Informe o peso em Kg da {c}ª pessoa: '))
    if sexo == 'F':
        total_mulheres += 1
        total_peso_mulheres += peso
    if sexo == 'M':
        if peso > 100:
            homens_mais100 += 1
        if peso > maior_peso:
            maior_peso = peso
if total_mulheres != 0:
    media_mulheres = total_peso_mulheres/total_mulheres
else:
    media_mulheres = 0
print(f'''a) {total_mulheres} mulheres foram cadastradas!
b) {homens_mais100} homens pesam mais de 100Kg
c) A média de peso entre as mulheres é de {media_mulheres:.2f}Kg
d) O maior peso entre os homens é de {maior_peso:.2f}Kg''')