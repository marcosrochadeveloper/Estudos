# Ex040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeira nota: 8
# Segunda nota: 5
# Tirando 8.0 e 5.0 a média do aluno é 6.5
# O aluno está em RECUPERAÇÃO.

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2} a média do aluno é {media}')
if media < 5:
    situacao = 'REPROVADO'
elif media < 7:
    situacao = 'em RECUPERAÇÃO'
else:
    situacao = 'APROVADO'
print(f'O aluno está {situacao}')