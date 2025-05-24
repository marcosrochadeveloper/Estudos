#17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo
#que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade-80)*5
    print(f'Multado! Deverá pagar uma multa no valor de R${multa:.2f}')
print('Dirija sempre com cuidado!')