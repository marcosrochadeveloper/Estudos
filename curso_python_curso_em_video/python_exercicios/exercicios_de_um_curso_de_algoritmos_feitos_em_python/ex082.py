# 82) Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. No final, mostre:
# a) Qual é a média da turma
# b) Quantos alunos estão acima da média da turma
# c) Qual foi a maior nota digitada
# d) Em que posições a maior nota aparece

notas = []
acima_da_media = 0
soma_notas = 0
maior_nota = None
posicoes_maior_nota = []
for c in range(10):
    notas.append(float(input(f'Informe a nota do {c+1}º aluno: ')))

for nota in notas:
    soma_notas += nota
    if maior_nota is None or maior_nota < nota:
        maior_nota = nota
media = soma_notas/10
c = 0
for nota in notas:
    if nota > media:
        acima_da_media += 1

    if nota == maior_nota:
        posicoes_maior_nota.append(c)
    c += 1


print(f'''a) A média da turma é {media}
b) {acima_da_media} alunos estão acima da média da turma
c) A maior nota digitada foi {maior_nota}
d) A maior nota foi digitada nas posicoes{posicoes_maior_nota} ''')