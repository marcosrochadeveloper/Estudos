#28) Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m².
#O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
#- Abaixo de 100m² = TERRENO POPULAR
#- Entre 100m² e 500m² = TERRENO MASTER
#- Acima de 500m² = TERRENO VIP
try:
    largura = float(input('Informe a largura do terreno em metros: '))
    comprimento = float(input('Informe o comprimento do terreno em metros: '))
    if largura > 0 or comprimento > 0:
        area = largura*comprimento
        if area < 100:
            classificacao = 'POPULAR'
        elif area <= 500:
            classificacao = 'MASTER'
        else:
            classificacao = 'VIP'
        print(f'O terreno informado tem {area:.2f}m² e por isso é classificado com um TERRENO {classificacao}!')
    else:
        print('Por favor informe um número real POSITIVO válido!')
except ValueError:
    print('Entrada inválida! Por favor, informe um número válido!')