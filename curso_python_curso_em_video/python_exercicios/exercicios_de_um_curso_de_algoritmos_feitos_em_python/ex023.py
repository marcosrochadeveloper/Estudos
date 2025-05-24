#23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres.
#Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto.
#Sabendo que: - Homens ganham 5% de desconto - Mulheres ganham 13% de desconto

nome = str(input('Qual seu nome? '))
sexo = str(input('Qual o seu sexo [M/F]: '))
valor = float(input('Qual o valor das compras? '))
desconto = 5 if sexo == 'M' else 13 #Desconto recebe 5 se sexo for igual a 'M' se não, recebe 13.
print(f'Olá {nome} suas compras no valor de R${valor:.2f} na promoção de dias das mães ficaram por R${valor-(valor*(desconto/100)):.2f}')