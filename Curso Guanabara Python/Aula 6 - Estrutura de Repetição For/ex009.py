# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime

menores = 0
maiores = 0

for c in range(1, 8):
    ano = int(input(f'Digite o {c}° ano de nascimento: '))
    if datetime.now().year - ano < 18:
        menores += 1
    else:
        maiores += 1

print(f'O numero de menores é {menores}\n'
      f'O numero de maiores é {maiores}')