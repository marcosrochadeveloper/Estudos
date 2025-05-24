#13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salário = float(input('Qual o salário atual? '))
print(f'Quem recebia R${salário:.2f} com o aumento de 15% passou a receber R${salário+(salário*0.15):.2f}')