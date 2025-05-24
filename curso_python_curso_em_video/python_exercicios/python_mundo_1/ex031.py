# Ex031 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual a distância da sua viagem? 150
# Sua viagem de 150.0Km custará R$75.00

# --------------------------------------------------------------

# Qual a distância da sua viagem? 210
# Sua viagem de 210.0Km custará R$94.50

distancia = float(input('Qual a distância da sua viagem? '))
<<<<<<< Updated upstream
custo_viagem = distancia * 0.5 if distancia <= 200 else distancia *0.45
print(f'Sua viagem de {distancia}Km custará R${custo_viagem:.2f}')
=======
precoKm = 0.5 if distancia <= 200 else 0.45
print(f'Sua viagem de \033[33m{distancia}Km\033[m custará \033[33mR${distancia * precoKm:.2f}\033[m')
>>>>>>> Stashed changes
