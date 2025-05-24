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
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
c = 0
total = 10
amais = 10
while c < 10:
    print(f'{termo} → ',end='')
    termo += razão
    c += 1
print('PAUSA')
while amais != 0:
    amais = int(input('Quantos termos você quer mostrar a mais? '))
    total += amais
    c = amais
    while c > 0:
        print(f'{termo} → ', end='')
        termo += razão
        c -= 1
    if amais != 0:
        print('PAUSA')
print(f'Progressão finalizada com {total} termos mostrados.')