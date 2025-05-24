# Ex044 - Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ============ LOJAS GUANABARA ============
# Preço das compras: R$1000
# FORMAS DE PAGAMENTO
# [ 1 ] à vista dinheiro/cheque
# [ 2 ] à vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão
# Qual é a opção? 3
# Sua compra será parcela em 2x de R$500.00 SEM JUROS
# Sua compra de R$1000.00 vai custar R$1000.00 no final.


print(f'{' LOJAS GUANABARA ':=^41}')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    novopreço = preço - (preço*0.1)
elif opção == 2:
    novopreço = preço - (preço*0.05)
elif opção == 3:
    novopreço = preço
    parcelas = preço / 2
    print(f'Sua compra será parcela em 2x de R${parcelas:.2f} SEM JUROS')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    novopreço = preço +(preço * 0.2)
    print(f'Sua compra será parcelada em {parcelas}x de R${novopreço/parcelas:.2f} COM JUROS')
else:
    novopreço = preço
    print('Opção Inválida, TENTE NOVAMENTE!')
print(f'Sua compra de R${preço:.2f} vai custar R${novopreço:.2f} no final.')