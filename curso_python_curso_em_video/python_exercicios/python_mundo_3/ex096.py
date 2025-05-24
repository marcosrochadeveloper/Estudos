# Ex096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
#
def area(comprimento, largura):
    print(f'A área de um terreno {comprimento}x{largura}m é de {comprimento*largura}m²')
print(' Controle de Terrenos')
print('-'*30)
c = float(input('COMPRIMENTO (m): '))
l = float(input('LARGURA de (m): '))
area(c, l)