# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

# Aula Anterior

valor_produto = float(input('Digite o valor do produto: '))

print('''\
Formas de pagamento:
[ 1 ] Dinheiro - 10% de desconto
[ 2 ] A vista no Cartão - 5% de desconto
[ 3 ] Parcelado 2x - preço normal
3x ou mais - 20% de juros''')

forma_de_pagamento = int(input('Digite uma forma de pagamento: '))

if forma_de_pagamento == 3:
    parcelado = int(input('Digite quantas parcelas: '))

if forma_de_pagamento == 1:
    print(f'O valor do produto é R${valor_produto:.2f} e o desconto para essa forma de pagamento é 10%. '
          f'Valor final é R${valor_produto - (valor_produto * 0.10):.2f}')
elif forma_de_pagamento == 2:
    print(f'O valor do produto é R${valor_produto:.2f} e o desconto para essa forma de pagamento é 5%. '
           f'Valor final é R${valor_produto - (valor_produto * 0.05):.2f}')
elif forma_de_pagamento == 3 and parcelado == 2:
    print(f'O valor do produto é R${valor_produto:.2f} e parcelado em 2x é R${valor_produto / 2:.2f}')
elif forma_de_pagamento == 3 and parcelado >= 3:
    juros = (valor_produto + (valor_produto * 0.20)) / parcelado
    print(f'O valor do produto é R${valor_produto:.2f} e parcelado em {parcelado}x vai ficar R${juros:.2f}. '
           f'O valor final com juros ficara R${valor_produto + (valor_produto * 0.20):.2f}')