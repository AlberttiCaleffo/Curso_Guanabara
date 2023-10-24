# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* vezes):
    print('Analisando os valores...', flush= True)
    sleep(2)
    if vezes == ():
        print(f'Foram informados 0. \nO maior valor é 0')
    else:
        for n in vezes:
            print(n, end=' ')
        print(f'Foram informados {len(vezes)}. \nO maior valor é {max(vezes)}')
        sleep(0.5)


maior(2, 9, 4, 5, 7, 1) 
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()