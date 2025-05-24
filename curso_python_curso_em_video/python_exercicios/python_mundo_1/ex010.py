# Ex010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere U$S1,00 = R$3,27
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Quanto dinheiro você tem na carteira? R$19.88
# Com R$19.88 você pode comprar US$6.08

dolares = 3.27
reais = float(input('Quanto dinheiro você tem na carteira? R$'))
<<<<<<< Updated upstream
print(f'Com R${reais:.2f} você pode comprar U${reais/dolares:.2f}')
=======
print(f'Com \033[33mR${reais:.2f}\033[m você pode comprar \033[33mUS${reais/dolares:.2f}\033[m')
>>>>>>> Stashed changes
