números = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if número < 0 or número > 20:
        print('Tente novamente.')
    else:
        break
print(f'Você digitou o número {números[número]}')