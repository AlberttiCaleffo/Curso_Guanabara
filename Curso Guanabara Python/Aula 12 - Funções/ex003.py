# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                     
# a) de 1 até 10, de 1 em 1                                                                                                
# b) de 10 até 0, de 2 em 2                                                                                                                                         
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, pula):
    if pula < 0:
        pula *= -1
    if pula == 0:
        pula = 1
    
    print(f'Contagem de {inicio} até {fim} de {pula} em {pula}')
    sleep(2.5)
    
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end= ' ', flush= True)
            sleep(0.5)
            inicio += pula
    else:
        while fim <= inicio:
            print(inicio, end= ' ', flush= True)
            sleep(0.5)
            inicio -= pula
    print('Fim!')
        
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
pula = int(input('Pula: '))

contador(inicio, fim, pula)