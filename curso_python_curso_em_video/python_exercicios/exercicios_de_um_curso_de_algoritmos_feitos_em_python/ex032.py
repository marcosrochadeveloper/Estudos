#32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
#jogador vai tentar descobrir qual foi o valor sorteado.
from random import randint
numero_pensado = randint(1,5)
try:
    tentativa = int(input('Pensei em um número inteiro entre 1 e 5 tente adivinhar: '))
    total = 0
    while True:
        total += 1
        if numero_pensado == tentativa:
            print(f'Parabéns, você acertou em {total} tentativas!')
            break
        else:
            if tentativa <= 0 or tentativa > 5:
                tentativa = int(input('NÚMERO INVÁLIDO! Digite um número inteiro entre 1 e 5: '))
            else:
                tentativa = int(input('ERROU! Tente outro número: '))
except ValueError:
    print('ENTRADA INVÁLIDA: Digite um número inteiro entre 1 e 5!')