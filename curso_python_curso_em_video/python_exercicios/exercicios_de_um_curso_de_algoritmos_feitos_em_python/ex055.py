# 55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32.
# A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar.
from random import randint
numsorted = randint(1,10)
print('Computador Escolheu um número!!!')
tentativas = 0
while True:
    jogador = int(input('Escolha um número entre 1 e 10: '))
    tentativas += 1
    if jogador == numsorted:
        print(f'Jogador acertou em {tentativas} tentativas')
        break
    if tentativas == 4:
        print(f'PERDEU! Errou 4 vezes!!! O número sorteado era {numsorted}')
        break
    print('ERROU! Tente Novamente!!!')
print('Finalizando...')