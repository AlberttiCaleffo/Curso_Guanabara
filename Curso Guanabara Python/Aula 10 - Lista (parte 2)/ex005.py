# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos = int(input('Digite quantos jogos você gostaria que eu gerasse: '))
palpites = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
contador = 1

print('=' * 10, f'Sorteando {jogos} jogos!', '=' * 10)

while jogos > 0:
    print(f'JOGO {contador}: {palpites}')
    palpites = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    jogos -= 1
    contador += 1
    sleep(1)

print('=' * 10, 'BOA SORTE!', '=' * 10)