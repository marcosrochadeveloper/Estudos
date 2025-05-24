# Ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Comprimento do cateto oposto: 5
# Comprimento do cateto adjacente: 6
# A hipotenusa vai medir 7.81
<<<<<<< Updated upstream
from math import hypot
cat_o = float(input('Comprimento do cateto oposto: '))
cat_a = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(cat_o, cat_a):.2f}')
#hipotenusa = (cat_o**2 + cat_a**2)**0.5
=======

from math import sqrt
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt(catetoOposto**2 + catetoAdjacente**2)
print(f'A hipotenusa vai medir \033[33m{hipotenusa:.2f}\033[m')
>>>>>>> Stashed changes
