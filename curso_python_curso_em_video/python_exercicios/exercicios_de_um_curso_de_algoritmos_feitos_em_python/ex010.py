#10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária
#para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))

print(f'Uma parede com {altura}x{largura} metros precisará de {altura*largura/2} litros de tinta para ser pintada!')