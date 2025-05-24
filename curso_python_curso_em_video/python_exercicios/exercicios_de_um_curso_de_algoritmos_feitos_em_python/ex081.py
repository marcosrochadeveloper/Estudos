# 81) Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No final, mostre:
# a) Qual é a média de idade das pessoas cadastradas
# b) Em quais posições temos pessoas com mais de 25 anos
# c) Qual foi a maior idade digitada (podem haver repetições)
# d) Em que posições digitamos a maior idade
idades = []
soma_idades = 0
posicoes_mais_25 = []
maior_idade = None
posicoes_maior = []
for c in range(8):
    idade = int(input(f'Informe a {c+1}ª idade: '))
    idades.append(idade)
    soma_idades += idade
    if idade > 25:
        posicoes_mais_25.append(c)
    if maior_idade is None or maior_idade < idade:
        maior_idade = idade
count = 0
for i in idades:
    if i == maior_idade:
        posicoes_maior.append(count)
    count += 1
media = soma_idades/8
print(f'''a) A média de idade das pessoas cadastradas é de aproximadamente {int(media)} anos
b) Temos {len(posicoes_mais_25)} pessoas com mais de 25 anos nas posições {posicoes_mais_25}
c) A maior idade digitada foi {maior_idade}
d) A maior idade foi digitada nas posições {posicoes_maior}''')