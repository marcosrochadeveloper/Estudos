#35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços.
# O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo.
# Além disso, o cliente paga por Km percorrido.
# Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos.
# No final mostre o preço a ser pago de acordo com a tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km

# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km
print('-----ALUGUEL DE CARROS-----')
while True:
    carro = int(input('[1] Carro Popular\n'
                      '[2] Carro de Luxo\n'
                      'Escolha uma opção: '))
    if carro == 1:
        diaria = 90
        menos = 0.20
        mais = 0.10
        ate = 100
        break
    elif carro == 2:
        diaria = 150
        menos = 0.30
        mais = 0.25
        ate = 200
        break
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
dias_alugados = int(input('O carro foi alugado por quantos dias? '))
km_percorridos = int(input('Durante esse tempo foram percorridos quantos kM? '))
if km_percorridos <= ate:
    total = diaria * dias_alugados + km_percorridos * menos
else:
    total = diaria * dias_alugados + km_percorridos * mais
print(f'O total a ser pago é R${total:.2f}')