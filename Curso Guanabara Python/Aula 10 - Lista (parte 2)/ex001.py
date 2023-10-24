# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

nomes_maiores = []
lista = []
dados = []
nomes_menores = []

while True:
    dados.append(input('Digite um nome: '))
    dados.append(float(input('Digite o peso:  ')))
    dados.reverse()
    lista.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if 'N' in continuar:
        break 

for resultado in lista:
    if max(lista)[0] == resultado[0]:
        nomes_maiores.append(resultado[1])
    if min(lista)[0] == resultado[0]:
        nomes_menores.append(resultado[1])

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso é {max(lista)[0]:.1f}Kg. Peso de {nomes_maiores}')
print(f'O maior peso é {min(lista)[0]:.1f}Kg. Peso de {nomes_menores}')

# print(f'O maior peso é {max(lista)[0]:.1f}Kg. Peso de {max(lista)[1]}')
# print(f'O menor peso é {min(lista)[0]:.1f}Kg. Peso de {min(lista)[1]}')