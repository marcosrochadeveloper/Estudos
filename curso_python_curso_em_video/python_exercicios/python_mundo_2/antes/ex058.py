# Ex058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Sou seu computador...
# Acabei de pensar em um número entre 0 e 10.
# Será que você consegue adivinhar qual foi?
# Qual é seu palpite? 5
# Menos... Tente mais uma vez.
# Qual é seu palpite? 1
# Menos... Tente mais uma vez.
# Qual é seu palpite? 0
# Acertou com 3 tentativas. Parabéns!

from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
número = randint(0,10)
tentativas = 0
palpite = ''
while número != palpite:
    palpite = int(input('Qual é seu palpite? '))
    if palpite < número:
        print('Mais... Tente mais uma vez.')
        tentativas += 1
    elif palpite > número:
        print('Menos... Tente mais uma vez.')
        tentativas += 1
    else:
        tentativas += 1
        print(f'Acertou com {tentativas} tentativas. Parabéns!')