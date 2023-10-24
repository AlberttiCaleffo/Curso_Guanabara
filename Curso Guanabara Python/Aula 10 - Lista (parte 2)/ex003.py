# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = []
valor = []
matriz_1 = c = 0

while True:
    valor.append(int(input(f'Digite um valor para [{matriz_1}, {c}]: ')))
    matriz.append(valor[:])
    valor.clear()
    c += 1
    if c == 3:
        matriz_1 += 1
        c = 0
    if matriz_1 == 3:
        break

for m in range(0, 9):
    print(f'[{matriz[m][0]:^5}]', end = '')
    if m == 2 or m == 5 or m == 8:
        print('')