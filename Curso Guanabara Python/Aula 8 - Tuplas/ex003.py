# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os numeros sorteados foram: ', end='')

for ordem_aleatoria in numeros_aleatorios:
    print(ordem_aleatoria, end=' ')

numeros_aleatorios = sorted(numeros_aleatorios)

print(f'\nO menor numero é : {numeros_aleatorios[0]}\n'
      f'O maior numero é: {numeros_aleatorios[-1]}')
