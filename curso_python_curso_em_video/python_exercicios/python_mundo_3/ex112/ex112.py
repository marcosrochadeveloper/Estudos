# Ex112 - Dentro do pacote utilidadesCeV1 que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)