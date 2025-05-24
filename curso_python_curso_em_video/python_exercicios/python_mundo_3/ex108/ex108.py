# Ex108 - Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from moeda import *

preco = str(input('Digite o preço: R$'))
if preco.count(',') == 1:
    preco = float(preco.replace(',', '.'))
else:
    preco = float(preco)

print(f'A metade de {moeda(preco)} é {metade(preco)}')
print(f'O dobro de {moeda(preco)} é {dobro(preco)}')
print(f'Aumentando 10%, temos {aumentar(preco)}')
print(f'Diminuindo 10%, temos {diminuir(preco)}')