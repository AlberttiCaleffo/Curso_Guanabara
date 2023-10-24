# Exercício Python 100: Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteia():
    for c in range(6):
        numeros.append(randint(1, 9))

def somando_par():
    soma_par = 0
    for par in numeros:
        if par % 2 == 0:
            soma_par += par
        else:
            continue
    return soma_par

sorteia()
somando_par()
print('Sorteando 5 valores da lista: ', end= ' ')
for numero in numeros:
    print(numero, end= ' ')
    sleep(1)
print('Pronto!')
print(f'Somando os valores pares de {numeros}, temos {somando_par()}')
