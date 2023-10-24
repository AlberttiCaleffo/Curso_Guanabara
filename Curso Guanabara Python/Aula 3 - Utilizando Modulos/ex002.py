from math import hypot

cateto_oposto = float(input('DIgite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

print(f'O comprimento da hipotenusa é {hypot(cateto_oposto, cateto_adjacente):.2f}')