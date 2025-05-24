# Ex007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeira nota do aluno: 5.5
# Segunda nota do aluno: 2
# A média entre 5.5 e 2.0 é igual a 3.8

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
<<<<<<< Updated upstream
media = (nota1+nota2)/2
print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}')
=======
print(f'A média entre \033[33m{nota1}\033[m e \033[33m{nota2}\033[m é igual a \033[33m{(nota1+nota2)/2:.1f}\033[m')
>>>>>>> Stashed changes
