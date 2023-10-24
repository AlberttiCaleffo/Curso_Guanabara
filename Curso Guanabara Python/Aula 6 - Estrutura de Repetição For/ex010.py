# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for c in range(1, 6):
    peso = float(input(f'{c}° peso: '))
    pesos += [peso]

pesos.sort()

print(f'O maior peso é {pesos[-1]:.1f}Kg\n'
      f'O menor peso é {pesos[0]:.1f}Kg')