# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_numeros = []

for c in range(0, 5): 
    numero = int(input(f'Digite o numero na posição {c}: '))
    lista_numeros.append(numero)

posicao_menor = lista_numeros.index(min(lista_numeros))
posicao_maior = lista_numeros.index(max(lista_numeros))
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

print(f'O maior valor é {maior_numero} e ele se encontra na posição {posicao_maior}', end='')
del lista_numeros[posicao_maior]
print(f'... {lista_numeros.index(max(lista_numeros), posicao_maior + 1)}...' if maior_numero in lista_numeros else '...')
print(f'O menor valor é {menor_numero} e ele se encontra na posição {posicao_menor}', end='')
del lista_numeros[posicao_menor]
print(f'... {lista_numeros.index(min(lista_numeros), posicao_menor + 1)}...' if menor_numero in lista_numeros else '...')
