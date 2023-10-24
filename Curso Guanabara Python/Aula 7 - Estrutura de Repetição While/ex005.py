# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA\n',
      '=-' * 14)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0

while contador < 10:
    print(f'{primeiro_termo}', end=' -> ')
    contador += 1
    primeiro_termo += razao

print('Fim')