número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
letras = str(número)
if opção == 1:
    #print(f'{número} convertido para BINÁRIO é igual a {número:b}')
    for c in range(len(letras)):
        if int(letras[c])**c < número:
            print(letras[c])
    print(f'{número} convertido para BINÁRIO é igual a {bin(número)[2:]}')
elif opção == 2:
    #print(f'{número} convertido para OCTAL é igual a {número:o}')
    print(f'{número} convertido para OCTAL é igual a {oct(número)[2:]}')
elif opção == 3:
    #print(f'{número} convertido para HEXADECIMAL é igual a {número:x}')
    print(f'{número} convertido para HEXADECIMAL é igual a {hex(número)[2:]}')
else:
<<<<<<< Updated upstream
    print('OPÇÃO INVÁLIDA! Tente novamente!')
=======
    print('OPÇÃO INVÁLIDA! Tente novamente!')
>>>>>>> Stashed changes
