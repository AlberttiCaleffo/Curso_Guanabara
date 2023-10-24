# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = int(input('Digite um numero de 0 a 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito','dezenove', 'vinte')

while True:
    if numero > 20:
        numero = int(input('Digite um numero valido. Digite um numero de 0 a 20: '))
    else:
        print(f'O numero que você digitou por extenso é {extenso[numero]}.')
        break