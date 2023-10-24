# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    base = l * c
    print(f'A area do terreno com largura de {l} e o comprimento de {c} é {base}m²')

print('Controle de Terrenos')  
print('-' * 30)  
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))    
area(l, c)