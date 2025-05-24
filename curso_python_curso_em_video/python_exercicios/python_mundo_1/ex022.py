<<<<<<< Updated upstream
'''
Ex022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
a) O nome com todas as letras maiúsculas.
b) O nome com todas as letras minúsculas.
c) Quantas letras ao todo (sem considerar espaços).
d) Quantas letras tem o primeiro nome.
[Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
Digite seu nome completo: José Antônio Pereira Albuquerque
Analisando seu nome...
a) Seu nome em maiúsculas é JOSÉ ANTÔNIO PEREIRA ALBUQUERQUE
b) Seu nome em minúsculas é josé antônio pereira albuquerque
c) Seu nome tem ao todo 29 letras
d) Seu primeiro nome é José e ele tem 4 letras
'''
from time import sleep
nome = str(input('Digite seu nome completo: ').strip())
total_letras = nome.split()
primeiro_nome = total_letras[0]
total_letras = "".join(total_letras)
print('Analisando seu nome...')
sleep(1)
print(f'''a) Seu nome em maiúsculas é {nome.upper()}
b) Seu nome em minúsculas é {nome.lower()}
c) Seu nome tem ao todo {len(total_letras)} letras
d) Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras
{nome.split()}''')
=======
# Ex022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas e minúsculas.
# b) Quantas letras ao todo (sem considerar espaços).
# c) Quantas letras tem o primeiro nome.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite seu nome completo: José Antônio Pereira Albuquerque
# Analisando seu nome...
# a) Seu nome em maiúsculas é JOSÉ ANTÔNIO PEREIRA ALBUQUERQUE
# a.2) Seu nome em minúsculas é josé antônio pereira albuquerque
# b) Seu nome tem ao todo 29 letras
# c) Seu primeiro nome é José e ele tem 4 letras

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'a) Seu nome em maiúsculas é \033[33m{nome.upper()}\033[m')
print(f'a.2) Seu nome em minúsculas é \033[33m{nome.lower()}\033[m')
nome = nome.split()
print(f'b) Seu nome tem ao todo \033[33m{len("".join(nome))}\033[m letras')
print(f'c) Seu primeiro nome é \033[33m{nome[0]}\033[m e ele tem \033[33m{len(nome[0])}\033[m letras')
>>>>>>> Stashed changes
