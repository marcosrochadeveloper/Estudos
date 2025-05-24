# Ex051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ==============================
#      10 TERMOS DE UMA PA
# ==============================
# Primeiro termo: 1
# Razão: 5
# 1 → 6 → 11 → 16 → 21 → 26 → 31 → 36 → 41 → 46 → ACABOU

print('='*30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range (0,10):
    print(termo, '→ ', end='')
    termo += razão
print('ACABOU')