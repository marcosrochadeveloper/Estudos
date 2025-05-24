# Ex027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite seu nome completo: Pedro da Silva Moreira
# Muito prazer em te conhecer Pedro!
# Seu primeiro nome é Pedro
# Seu último nome é Moreira

<<<<<<< Updated upstream
nome = str(input('Digite seu nome completo: '))
=======
nome = str(input('Digite seu nome completo: ')).strip()
>>>>>>> Stashed changes
nome = nome.split()
print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {nome[0]}
Seu último nome é {nome[len(nome)-1]}''')