# Ex009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número para ver sua tabuada: 6
# -------------
# 6 x  1 = 6
<<<<<<< Updated upstream
# 6 x  2 = 12
# 6 x  3 = 18
# 6 x  4 = 24
# 6 x  5 = 30
# 6 x  6 = 36
# 6 x  7 = 42
# 6 x  8 = 48
# 6 x  9 = 54
# 6 x 10 = 60
# -------------

num = int(input('Digite um número para ve sua tabuada: '))
print(f'''-------------
{num} x  1 = {num*1}
{num} x  2 = {num*2}
{num} x  3 = {num*3}
{num} x  4 = {num*4}
{num} x  5 = {num*5}
{num} x  6 = {num*6}
{num} x  7 = {num*7}
{num} x  8 = {num*8}
{num} x  9 = {num*9}
{num} x 10 = {num*10}
-------------''')
=======
# 6 x  2 =  12
# 6 x  3 =  18
# 6 x  4 =  24
# 6 x  5 =  30
# 6 x  6 =  36
# 6 x  7 =  42
# 6 x  8 =  48
# 6 x  9 =  54
# 6 x 10 =  60
# -------------

numero = int(input('Digite um número para ver sua tabuada: '))
print(f'\033[33m{'-'*13}\033[m')
print(f'{numero} \033[33mx\033[m  1 \033[33m=\033[m {numero*1}')
print(f'{numero} \033[33mx\033[m  2 \033[33m=\033[m  {numero*2}')
print(f'{numero} \033[33mx\033[m  3 \033[33m=\033[m  {numero*3}')
print(f'{numero} \033[33mx\033[m  4 \033[33m=\033[m  {numero*4}')
print(f'{numero} \033[33mx\033[m  5 \033[33m=\033[m  {numero*5}')
print(f'{numero} \033[33mx\033[m  6 \033[33m=\033[m  {numero*6}')
print(f'{numero} \033[33mx\033[m  7 \033[33m=\033[m  {numero*7}')
print(f'{numero} \033[33mx\033[m  8 \033[33m=\033[m  {numero*8}')
print(f'{numero} \033[33mx\033[m  9 \033[33m=\033[m  {numero*9}')
print(f'{numero} \033[33mx\033[m 10 \033[33m=\033[m  {numero*10}')
print(f'\033[33m{'-'*13}\033[m')
>>>>>>> Stashed changes
