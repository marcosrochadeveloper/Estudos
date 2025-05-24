# Ex006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e raiz quadrada.
<<<<<<< Updated upstream
#[DICA]:
# Qualquer número elevado a 0.5 resultará em sua raiz quadrada por exemplo:
# 85**0.5 vai ser igual a 9.22 || 81**0.5 vai ser igual a 9
=======
>>>>>>> Stashed changes
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 85
# O dobro de 85 vale 170.
# O triplo de 85 vale 255.
# A raiz quadrada de 85 é igual a 9.22.

<<<<<<< Updated upstream
num = int(input('Digite um número: '))
print(f'''O dobro de {num} vale {num*2}
O triplo de {num} vale {num*3}
A raiz quadrada de {num} é igual a {num**0.5:.2f}''')
=======
#[DICA]:
# Qualquer número elevado a 0.5 resultará em sua raiz quadrada por exemplo:
# 85**0.5 vai ser igual a 9.22

from math import sqrt
numero = int(input('Digite um número: '))
print(f'O dobro de \033[33m{numero}\033[m vale \033[33m{numero*2}\033[m.')
print(f'O triplo de \033[33m{numero}\033[m vale \033[33m{numero*3}\033[m.')
print(f'A raiz quadrada de \033[33m{numero}\033[m é igual a \033[33m{sqrt(numero):.2f}\033[m.')

>>>>>>> Stashed changes
