# Ex019 - Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro aluno: João
# Segundo aluno: Maria
# Terceiro aluno: Josefa
# Quarto aluno: Pedro
# O aluno escolhido foi Josefa

from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido foi {choice(alunos)}')