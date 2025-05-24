#42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo qualquer e mostre uma contagem até esse valor:
#Ex: Digite um valor: 35
#Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

num = int(input('Informe um número inteiro: '))
c = 1
while c < num+1:
    print(c, end=' ')
    c += 1
print('Acabou!')