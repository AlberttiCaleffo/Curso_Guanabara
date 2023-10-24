# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('A', 'E', 'I', 'O', 'U')
contador = 0

for palavra in palavras:
    contador = 0
    print(f'\nNa palavra {palavra} temos', end=' ')
    while contador < len(palavra):
        if palavra[contador] in vogais:
            print(f'{palavra[contador]}', end=' ')
            contador += 1
        else:
            contador += 1
            continue
