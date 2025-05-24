# Ex109 - Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from moeda import *

preco = str(input('Digite o preço: R$'))
if preco.count(',') == 1:
    preco = float(preco.replace(',', '.'))
else:
    preco = float(preco)


print(f'A metade de {moeda(preco, False)} é {metade(preco)}')
print(f'O dobro de {moeda(preco)} é {dobro(preco)}')
print(f'Aumentando 10%, temos {aumentar(preco)}')
print(f'Diminuindo 10%, temos {diminuir(preco)}')