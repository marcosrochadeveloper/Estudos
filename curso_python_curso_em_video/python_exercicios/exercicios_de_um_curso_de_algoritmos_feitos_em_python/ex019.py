#19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela.
#No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).

nome = str(input('Nome do aluno: '))
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))

média = (nota1+nota2) / 2

print(f'O aluno {nome} obteve uma média de {média:.1f}.')

if média >= 7:
    print('O aluno foi APROVADO!')
else:
    print('O aluno foi REPROVADO!')