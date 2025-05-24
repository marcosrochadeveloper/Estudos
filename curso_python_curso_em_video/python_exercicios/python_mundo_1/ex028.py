# Ex028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Vou pensar em um número entre 0 e 5. Tente adivinhar...
# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Em que número eu pensei? 3
# PROCESSANDO...
# GANHEI! Eu pensei no número 1 e não no 3!

# -------------------------------------------------------------

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Vou pensar em um número entre 0 e 5. Tente adivinhar...
# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Em que número eu pensei? 0
# PROCESSANDO...
# PARABÉNS! Você conseguiu me vencer!

<<<<<<< Updated upstream
from random import randint
from time import sleep
print(f'''{'-=-' * 20}
 Vou pensar em um número entre 0 e 5. Tente adivinhar...
{'-=-' * 20}''')
computador = randint(0,5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if num == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
=======
from time import sleep
from random import randint
print('\033[33m-=-\033[m'*19)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m'*19)
numeropensado = randint(0,5)
numero = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
if numeropensado == numero:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')
>>>>>>> Stashed changes
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {num}!')
