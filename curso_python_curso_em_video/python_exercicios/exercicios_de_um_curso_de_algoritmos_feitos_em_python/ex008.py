#8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
#Ex:
#Digite uma distância em metros: 185.72
#A distância de 85.7m corresponde a:
#0.18572Km
#1.8572Hm
#18.572Dam
#1857.2dm
#18572.0cm
#185720.0mm

distância = float(input('Digite uma distância em metros: '))
print(f'A distância de {distância}m corresponde a: ')
print(f'{distância/1000}Km')
print(f'{distância/100}Hm')
print(f'{distância/10}Dam')
print(f'{distância*10}dm')
print(f'{distância*100}cm')
print(f'{distância*1000}mm')