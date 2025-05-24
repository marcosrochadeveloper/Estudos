#9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,45.

reais = float(input('Quanto você tem em R$? '))
print(f'Tendo R${reais:.2f} você pode comprar US${reais/3.45:.2f}')