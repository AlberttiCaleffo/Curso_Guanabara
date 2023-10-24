# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

conjunto = []

for c in range(0, 5):
    if c == 0 or c == 3:
        numero = int(input('Digite um numero: '))
        conjunto.append(numero)
        print('Adicionado ao final da lista')
    elif c == 4:
        numero = int(input('Digite um numero: '))
        conjunto.append(numero)
        print('Adicionado na posição 0')
    else:
        numero = int(input('Digite um numero: '))
        conjunto.append(numero)
        print(f'Adicionado na posição {c - 1}')
print(sorted(conjunto))