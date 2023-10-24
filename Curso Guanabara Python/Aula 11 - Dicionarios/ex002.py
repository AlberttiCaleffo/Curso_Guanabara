# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
contador = 1

for c in range(1, 5):
    jogadores[f'Jogadores_{c}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(1)

print('=-' * 10, 'RANKING', '=-' * 10)

ranking = sorted(jogadores.items(), key= itemgetter(1), reverse= True)

for k, v in ranking:
    print(f'{contador} - {k} ganhou com {v}')
    contador += 1
    sleep(1)