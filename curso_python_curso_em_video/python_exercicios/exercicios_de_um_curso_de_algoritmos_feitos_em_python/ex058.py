# 58) Faça um algoritmo que leia a idade de vários alunos de uma turma.
# O programa vai parar quando for digitada a idade 999.
# No final, mostre quantos alunos existem na turma e qual é a média de idade do grupo.

total = alunos = 0
while True:
    idade = int(input(f'Informe a idade do {alunos+1}º aluno: '))
    if idade == 999:
        break
    total += idade
    alunos += 1
media = total / alunos
print(f'A turma tem {alunos} alunos, e a média de idade é de aproximadamente {int(media)} anos.')