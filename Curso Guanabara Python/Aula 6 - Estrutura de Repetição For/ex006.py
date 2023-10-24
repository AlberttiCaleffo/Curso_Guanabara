# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
# mostre os 10 primeiros termos dessa progressão.

print('=' * 20,
      '\n10 termos de um PA\n',
      '=' * 20)

termo_1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))

for c in range(0, 10):
    print(f'{termo_1}', end=' -> ')
    termo_1 += razao
print('ACABOU!')