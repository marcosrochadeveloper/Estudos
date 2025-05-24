#Ex015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Quantos dias alugados? 5
# Quantos Km Rodados? 200
# O total a pagar é de R$330.00

<<<<<<< Updated upstream
diasalugados = int(input('Quantos dias alugados? '))
kmrodados = int(input('Quantos Km Rodados? '))
total = diasalugados*60 + kmrodados*0.15
print(f'O total a pagar é de R${total:.2f}')
=======
diasAlugados = int(input('Quantos dias alugados? '))
kmRodados = int(input('Quantos Km Rodados? '))
valorTotal = diasAlugados*60 + kmRodados*0.15
print(f'O total a pagar é de \033[33mR${valorTotal:.2f}\033[m')
>>>>>>> Stashed changes
