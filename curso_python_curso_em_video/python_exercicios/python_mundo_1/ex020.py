# Ex020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
<<<<<<< Updated upstream
# Primeiro aluno: João
# Segundo aluno: Maria
# Terceiro aluno: Josefa
# Quarto aluno: Pedro
# A ordem de apresentação será:
# ['Pedro', 'Maria', 'Josefa', 'João']
=======
# Primeiro aluno: Pedro
# Segundo aluno: Pablo
# Terceiro aluno: Petrus
# Quarto aluno: Pietro
# A ordem de apresentação será:
# ['Petrus', 'Pablo', 'Pietro', 'Pedro']

>>>>>>> Stashed changes
from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
<<<<<<< Updated upstream
print('A ordem de apresentação será: ')
print(alunos)
=======
print('A ordem de apresentação será:')
print(f'{alunos}')
>>>>>>> Stashed changes
