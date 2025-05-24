# 69) [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética),
# mostrando na tela os 10 primeiros elementos da PA e a soma entre todos os valores da sequência.

primeiro = int(input('Informe o primeiro termo para uma PA(Progressão Aritmética): '))
razao = int(input('Informe a razão para o calculo dessa PA: '))
soma = 0
for c in range(10):
    print(primeiro, end=' ')
    primeiro += razao
    if c < 9:
        soma += primeiro
print()
print(f'A soma entre todos os valores foi {soma}')