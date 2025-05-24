#30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais
#- ESCALENO: todos os lados diferentes
try:
    segmentos = []
    for c in range(1,4):
        segmentos.append(float((input(f'Informe o {c}º segmento: '))))
    if segmentos[0] == segmentos[1] == segmentos[2]:
        tipo = 'Equilátero'
    elif segmentos[0] != segmentos[1] and segmentos[0] != segmentos[2] and segmentos[1] != segmentos[2]:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'
    if segmentos[0] < segmentos[1] + segmentos[2] and segmentos[1] < segmentos[0] + segmentos[2] and segmentos[2] < segmentos[0] + segmentos[1]:
        print(f'Com os segmentos {segmentos} é possível formar um triângulo {tipo}!')
    else:
        print(f'Com os segmentos {segmentos} não é possível formar um triângulo!')
except ValueError:
    print('Entrada inválida! Por favor informe valores reais válidos!')