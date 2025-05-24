# Ex025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é seu nome completo? Mario da Silva Mendonça
# Seu nome tem Silva? True
# ---------------------------------------------

<<<<<<< Updated upstream
nome = str(input('Qual é o seu nome completo? ' ).upper())
print(f'Seu nome tem Silva? {'SILVA' in nome}')
=======
nome = str(input('Qual é seu nome completo? '))
silva = 'silva' in nome.lower()
if silva:
    silva = '\033[32mTrue\033[m'
else:
    silva = '\033[31mFalse\033[m'
print(f'Seu nome tem Silva? {silva}')
>>>>>>> Stashed changes
