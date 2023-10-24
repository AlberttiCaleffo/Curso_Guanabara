# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = input('Digite um frase: ').upper().strip() 
frase = frase.replace(' ', '')

print(f'O inverso da frase {frase} é {frase[::-1]}')
if frase == frase[::-1]:
    print('É Palíndromo.')
else:
    print('Não é Palíndromo.')