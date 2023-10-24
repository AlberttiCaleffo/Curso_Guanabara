# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

def maior(vezes ,quant, valor):
    valor = []
    for c in range(vezes):
        print('-=' * 30)
        print('Analisando valores passados...', flush= True)
        sleep(2)
        for c in range(quant):
            valor.append(randint(0, 9))
        for n in valor:
            print(f'{n}', end= ' ')
        print(f'Foram analisados {len(valor)} valores. \nO maior valor é {max(valor)}')
        valor.clear()
        quant = randint(1, 6)
        sleep(1)

valor_aleatorio = randint(0, 9)
quant_aleatorio = randint(1, 6)

maior(5, quant_aleatorio, valor_aleatorio)