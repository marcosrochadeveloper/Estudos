# 85) Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e guarde esses dados em três vetores.
# No final, mostre uma listagem contendo apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.

nomes = []
sexos = []
salarios = []
nomes_mulheres = []
salarios_mulheres = []
for c in range(5):
    nomes.append(str(input(f'Informe o nome da {c+1}ª pessoa: ')))
    sexos.append(str(input(f'Informe o sexo da {c + 1}ª pessoa [M/F]: ').upper()))
    salarios.append(float(input(f'Informe o salário da {c + 1}ª pessoa: R$')))
for c in range(5):
    if sexos[c] == 'F' and salarios[c] > 5000:
        nomes_mulheres.append(nomes[c])
        salarios_mulheres.append(salarios[c])
print(f'Entre os 5 funcionários informados, tem {len(nomes_mulheres)} mulher(es) que ganha(m) mais de R$5 mil.')
if len(nomes_mulheres) > 0:
    for c in range(len(nomes_mulheres)):
        print(f'{nomes_mulheres[c]} ganha R${salarios_mulheres[c]:.2f}')