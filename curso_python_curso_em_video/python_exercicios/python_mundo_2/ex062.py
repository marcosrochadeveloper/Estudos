# Ex062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Gerador de PA
# -=-=-=-=-=-=-=-=-=-=
# Primeiro termo: 1
# Razão da PA: 3
# 1 → 4 → 7 → 10 → 13 → 16 → 19 → 22 → 25 → 28 → PAUSA
# Quantos termos você quer mostrar a mais? 5
# 31 → 34 → 37 → 40 → 43 → PAUSA
# Quantos termos você quer mostrar a mais? 0
# Progressão finalizada com 15 termos mostrados.
print('Gerador de PA')
print('-='*10)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = total = 10
c = 0
while termos != 0:
    while c < termos:
        print(termo1, end=' → ')
        termo1 += razao
        c += 1
    print('PAUSA')
    c = 0
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    total += termos
print(f'Progressão finalizada com {total} termos mostrados.')