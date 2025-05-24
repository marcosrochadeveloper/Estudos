#16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
#fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
#quantos dias de vida um fumante perderá e exiba o total em dias.

porDia = int(input('Quantos cigarros fuma por dia? '))
anosFumando = int(input('Fazem quantos anos que fuma? '))
totalCigarros = porDia * anosFumando * 365
diasPerdidos = totalCigarros / 144
print(f'Você perdeu {diasPerdidos:.2f} dias de vida pelo tempo que já passou fumando!')