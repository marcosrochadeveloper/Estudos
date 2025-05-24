# Ex107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from moeda import *

preco = float(input('Digite o preço: R$'))

print(f'A metade de R${preco:.2f} é R${metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${dobro(preco):.2f}')
print(f'Aumentando 10%, temos R${aumentar(preco):.2f}')
print(f'Diminuindo 10%, temos R${diminuir(preco):.2f}')