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
print(f'{' LOJAS GUANABARA ':=^40}')
preco = float(input('Preço das compras: R$'))
opcao = int(input(f'''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if opcao == 1:
    preco_final = preco - (preco*0.1)
    print('Você vai pagar em dinheiro/cheque e terá 10% de desconto.')
elif opcao == 2:
    preco_final = preco - (preco*0.05)
    print('Você vai pagar no cartão à vista e terá 5% de desconto.')
elif opcao == 3:
    preco_final = preco
    print(f'Sua compra será parcelada em 2x de R${preco/2:.2f} SEM JUROS')
elif opcao == 4:
    vezes = int(input('Em quantas vezes? '))
    preco_final = preco + (preco*0.20)
    print(f'Sua compra será parcelada em {vezes} vezes de R${preco_final/vezes:.2f} COM JUROS')
else:
    print('OPÇÃO INVÁLIDA, ENCERRANDO....')
if opcao > 0 and opcao < 5:
    print(f'Sua compra de R${preco:.2f} vai custar R${preco_final:.2f} no final')
