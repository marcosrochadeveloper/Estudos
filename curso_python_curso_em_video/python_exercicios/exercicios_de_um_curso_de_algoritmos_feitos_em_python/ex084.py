# 84) Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses valores em dois vetores, em posições relacionadas.
# No final, mostre uma listagem contendo apenas os dados das pessoas menores de idade.

nomes = []
idades = []
nomes_menores = []
idades_menores = []
for c in range(9):
    nomes.append(str(input(f'Informe o nome da {c+1}ª pessoa: ')))
    idades.append(int(input(f'Informe a idade da {c+1}ª pessoa: ')))


for c in range(9):
    if idades[c] < 18:
        nomes_menores.append(nomes[c])
        idades_menores.append(idades[c])

print(f'Foram informadas {len(idades_menores)} pessoas com menos de 18 anos.')
for c in range(len(idades_menores)):
    print(f'{nomes_menores[c]} com {idades_menores[c]} anos')