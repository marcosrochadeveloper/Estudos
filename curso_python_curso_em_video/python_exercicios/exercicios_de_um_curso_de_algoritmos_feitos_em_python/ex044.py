#44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
#incremento, mostrando em seguida todos os valores no intervalo:
#Ex: Digite o primeiro Valor: 3
#Digite o último Valor: 10
#Digite o incremento: 2
#Contagem: 3 5 7 9 Acabou!

primeiro_valor = int(input('Digite o primeiro Valor: '))
ultimo_valor = int(input('Digite o último Valor: '))
incremento = int(input('Digite o incremento: '))
c = primeiro_valor
print('Contagem: ', end='')
while c < ultimo_valor:
    print(c, end=' ')
    c += incremento
print('Acabou!')