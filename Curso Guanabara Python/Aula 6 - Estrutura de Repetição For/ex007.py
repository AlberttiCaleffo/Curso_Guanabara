# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um numero: '))
divisivel = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[033m{c}\033[033m', end=' ')
        divisivel += 1
    else:
        print(f'\033[031m{c}\033[031m', end=' ')

print(f'\nO numero {numero} é divisivel {divisivel} vezes.')

if divisivel == 2:
    print('O valor é PRIMO!')
else:
    print('O valor NÃO é PRIMO!')