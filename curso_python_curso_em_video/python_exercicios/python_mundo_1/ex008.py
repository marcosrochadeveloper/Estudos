# Ex008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros, entre outras medidas de tamanhos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Uma distância em metros: 3
# A medida de 3.0m corresponde a:
# 0.003km
# 0.03hm
# 0.3dam
# 30dm
# 300cm
# 3000mm

<<<<<<< Updated upstream
distancia = float(input('Uma distância em metros: '))
print(f'''A medida de {distancia}m corresponde a:
{distancia/1000}km
{distancia/100}hm
{distancia/10}dam
{distancia*10:.0f}dm
{distancia*100:.0f}cm
{distancia*1000:.0f}mm''')
=======
distância = float(input('Uma distância em metros: '))
print(f'A medida de \033[33m{distância}m\033[m corresponde a:')
print(f'\033[33m{distância/1000}km')
print(f'{distância/100}hm')
print(f'{distância/10}dam')
print(f'{distância*10:.0f}dm')
print(f'{distância*100:.0f}cm')
print(f'{distância*1000:.0f}mm')
>>>>>>> Stashed changes
