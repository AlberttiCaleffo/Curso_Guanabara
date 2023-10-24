# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

matriz = []
valor = []
par = []
soma_coluna3 = []
maior_linha2 = []
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
    if matriz[m][0] % 2 == 0:
        par.append(matriz[m][0])
    if m <= 5 and m >= 3:
        maior_linha2.append(matriz[m][0])
    if m == 2 or m == 5 or m == 8:
        soma_coluna3.append(matriz[m][0])
        print('')

print(f'A soma de todos os numeros pares é: {sum(par)}')
print(f'A soma dos valores da terceira coluna é: {sum(soma_coluna3)}')
print(f'O maior valor da segunda linha é: {max(maior_linha2)}')