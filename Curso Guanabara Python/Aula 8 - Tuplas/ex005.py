# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (('Lapis', 1.75), ('Borracha', 2.00), ('Caderno', 15.90), ('Estojo', 25.00),
            ('Transferidor', 4.20), ('Compasso', 9.99), ('Mochila', 120.32), ('Canetas', 22.30))
contador = 0

while contador < len(produtos):
    print(f'{produtos[contador][0]:.<12}', end='')
    print('.' * 20, end='')
    print(f'R$ {produtos[contador][1]:>6.2f}')
    contador += 1
