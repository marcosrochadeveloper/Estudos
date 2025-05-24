# Ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite algo: Programador
# O tipo primitivo desse valor é <class 'str'>
# Só tem espaços?   False
# É um número?   False
# É alfabético?   True
# É alfanumérico?   True
# Está em maiúsculas?   False
# Está em minúsculas?   False
# Está capitalizada?   True

<<<<<<< Updated upstream
info = input('Digite algo: ')
print(f'''O tipo primitivo desse valor é {type(info)}
Só tem espaços? {info.isspace()}
É um número? {info.isnumeric()}
É alfabético? {info.isalpha()}
É alfanumérico? {info.isalnum()}
Está em maiúsculas? {info.isupper()}
Está em minúsculas? {info.islower()}
Está capitalizada? {info.istitle()}''')
=======
palavra = input('Digite algo: ')
fim = '\033[m'
verde = '\033[32m'
vermelho = '\033[31m'
space = verde if palavra.isspace() == True else vermelho
numeric = verde if palavra.isnumeric() == True else vermelho
alpha = verde if palavra.isalpha() == True else vermelho
alnum = verde if palavra.isalnum() == True else vermelho
upper = verde if palavra.isupper() == True else vermelho
lower = verde if palavra.islower() == True else vermelho
title = verde if palavra.istitle() == True else vermelho
print(f'O tipo primitivo desse valor é \033[33m{type(palavra)} {fim}')
print(f'Só tem espaços? {space} {palavra.isspace()} {fim}')
print(f'É um número? {numeric} {palavra.isnumeric()} {fim}')
print(f'É alfabético? {alpha} {palavra.isalpha()} {fim}')
print(f'É alfanumérico? {alnum} {palavra.isalnum()} {fim}')
print(f'Está em maiúsculas? {upper} {palavra.isupper()} {fim}')
print(f'Está em minúsculas? {lower} {palavra.islower()} {fim}')
print(f'Está capitalizada? {title} {palavra.istitle()} {fim}')
>>>>>>> Stashed changes
