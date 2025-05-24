#25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
#Analise seus comprimentos e diga se é possível formar um triângulo com essas retas.
#Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.

segmentos = []
for c in range(1,4):
    segmentos.append(float((input(f'Informe o {c}º segmento: '))))
if segmentos[0] < segmentos[1] + segmentos[2] and segmentos[1] < segmentos[0] + segmentos[2] and segmentos[2] < segmentos[0] + segmentos[1]:
    print(f'Com os segmentos {segmentos} é possível formar um triângulo!')
else:
    print(f'Com os segmentos {segmentos} não é possível formar um triângulo!')