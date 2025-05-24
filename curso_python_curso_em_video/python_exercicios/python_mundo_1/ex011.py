# Ex011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Largura da parede: 2.5
# Altura da parede: 1.75
<<<<<<< Updated upstream
# Sua parede tem a dimensão de 2.5x1.75m e sua área é de 4.375m².
=======
# Sua parede tem a dimensão de 2.5x1.75 e sua área é de 4.375m².
>>>>>>> Stashed changes
# Para pintar essa parede, você precisará de 2.1875l de tinta

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura*largura
print(f'Sua parede tem a dimensão de {altura}x{largura}m e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede você precisará de aproximadamente {area/2:.2f}l de tinta')
