# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

total = contador = preco_antigo = 0
produto_barato = ''

while True:
    nome_produto = input('Nome do produto: ').strip()
    preco_produto = float(input('Preço do produto: '))
    continuar = input('Quer inserir mais itens? [S/N]: ').strip().lower()
    total += preco_produto
    if preco_produto < preco_antigo or preco_antigo == 0:
        produto_barato = nome_produto
        preco_antigo = preco_produto        
    else: 
        pass
    if preco_produto > 1000:
        contador += 1
    else:
        pass
    if continuar in 'sim':
        continue
    else:
        break

print(f'O valor total da compra é R${total:.2f}.\n'
      f'Existem {contador} produto(s) acima de R$1000,00.\n'
      f'O produto mais barato é {produto_barato} no valor de R${preco_antigo:.2f}')
