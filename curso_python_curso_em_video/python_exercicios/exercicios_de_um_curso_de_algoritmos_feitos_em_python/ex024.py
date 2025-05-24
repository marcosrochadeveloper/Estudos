#24) Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.

distância = float(input('Qual distância você irá percorrer? '))
preço = distância * 0.45 if distância > 200 else distância * 0.5
print(f'Para uma viagem de {distância}kM o preço da passagem será R${preço:.2f}')