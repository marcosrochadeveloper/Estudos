# Ex089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
alunos = []
aluno = []
resposta = 'S'
while resposta != 'N':
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno[:])
    aluno.clear()
    resposta = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    while resposta not in 'SN':
        resposta = str(input('RESPOSTA INVÁLIDA! Quer continuar? [S/N]: ').strip().upper()[0])
print('-='*30)
print('No. NOME         MÉDIA')
print('-'*26)
for e, a in enumerate(alunos):
    print(f'{e}   {a[0]:<12}{(a[1]+a[2])/2:>6.1f}')
print('-'*32)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'Notas de {alunos[mostrar][0]} são {alunos[mostrar][1:3]}')
    print('-' * 32)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')