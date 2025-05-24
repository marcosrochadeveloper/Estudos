# 63) Crie um programa usando a estrutura “faça enquanto” que leia vários números.
# A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares
soma_valores = quantidade_valores = pares = 0
menor_valor = None
while True:
    num = int(input('Digite um número: '))

    soma_valores += num

    if menor_valor is None or menor_valor > num:
        menor_valor = num

    quantidade_valores += 1

    if num%2 == 0:
        pares += 1
    continuar = str(input('Quer continuar [S/N]? ').upper())
    if continuar == 'N':
        break
print(f'''a) A soma de todos os valores foi de {soma_valores}
b) O menor valor digitado foi {menor_valor}
c) A média entre todos os valores foi de {soma_valores/quantidade_valores:.2f}
d) {pares} valores são par''')