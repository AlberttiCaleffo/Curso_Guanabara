# Exercício Python 102: Crie um programa que tenha uma função fatorial() 
# que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

numero = int(input('Digite o numero a qual vai ser dado o fatorial: '))
booleano = bool(input('Digite enter para Falso, ou digite algo mais enter para Verdadeiro: '))
resultado = 1

def fatorial(numero, show= False):
    '''Fatorial(numero, show= False)
    '''
    for facto in reversed(range(1, numero + 1)):
        global resultado 
        resultado *= facto
    if show:
        for facto in reversed(range(1, numero + 1)):
            print(f'{facto} x ', end= '')
            if facto == 1:
                print(f'{facto} = {resultado}')
    else:
        print(resultado)

fatorial(numero, booleano)
help(fatorial)