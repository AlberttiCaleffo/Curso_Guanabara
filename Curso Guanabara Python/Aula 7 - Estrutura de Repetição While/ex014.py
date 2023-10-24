# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

dinheiro = int(input('Digite o valor a ser sacado: '))
contador_50 = contador_20 = contador_10 = contador_1 = 0

while dinheiro >= 50:
    dinheiro -= 50
    contador_50 += 1
while dinheiro >= 20:
    dinheiro -= 20
    contador_20 += 1
while dinheiro >= 10:
    dinheiro -= 10
    contador_10 += 1
while dinheiro >= 1:
    dinheiro -= 1
    contador_1 += 1

print('=' * 20)

if contador_50 != 0:
    print(f'Total de {contador_50} de R$50')
else:
    pass
if contador_20 != 0:
    print(f'Total de {contador_20} de R$20')
else:
    pass
if contador_10 != 0:
    print(f'Total de {contador_10} de R$10')
else:
    pass
if contador_1 != 0:
    print(f'Total de {contador_1} de R$1')
else:
    pass

print('=' * 20)
