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
média = (nota1+nota2)/2
print(f'Tirando {nota1:.1f} e {nota2:.1f} a média do aluno é {média:.1f}')
if média < 5:
    print('O aluno está REPROVADO.')
elif 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')