# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('=' * 10, 'Jogo do JOKENPÔ!', '=' * 10)

print('Opções de jogada:')
print('[0] TESOURA\n'
      '[1] PEDRA\n'
      '[2] PAPEL')

jogador = int(input('Escolha uma opção contra a maquina: '))
computador = randint(0, 2)

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!')

if computador == jogador or computador == jogador or computador == jogador:
    if computador == 0:
        print('A maquina escolheu TESOURA!\n'
              'Você escolheu TESOURA!\n',
              '=' * 10, 'Deu EMPATE...', '=' * 10)
    elif computador == jogador:
        print('A maquina escolheu PEDRA!\n'
              'Você escolheu PEDRA\n',
              '=' * 10, 'Deu EMPATE...', '=' * 10)
    elif computador == jogador:
        print('A maquina escolheu PAPEL\n'
              'Você escolheu PAPEL\n',
              '=' * 10, 'Deu EMPATE...', '=' * 10)
elif jogador == 0 and computador == 1:
    print('O computador escolheu PEDRA!\n'
          'Você escolheu TESOURA!\n',
          '=' * 10, 'VOCÊ PERDEU!', '=' * 10)
elif jogador == 0 and computador == 2:
    print('O computador escolheu PAPEL!\n'
          'Você escolheu TESOURA!\n',
          '=' * 10, 'VOCÊ GANHOU!', '=' * 10)
elif jogador == 1 and computador == 0:
    print('O computador escolheu TESOURA!\n'
          'Você escolheu PEDRA!\n',
          '=' * 10, 'VOCÊ GANHOU!', '=' * 10)
elif jogador == 1 and computador == 2:
    print('O computador escolheu PAPEL!\n'
          'Você escolheu PEDRA!\n',
          '=' * 10, 'VOCÊ PERDEU!', '=' * 10)
elif jogador == 2 and computador == 0:
    print('O computador escolheu TESOURA!\n'
          'Você escolheu PAPEL!\n',
          '=' * 10, 'VOCÊ PERDEU!', '=' * 10)
elif jogador == 2 and computador == 1:
    print('O computador escolheu PEDRA!\n'
          'Você escolheu PAPEL!\n',
          '=' * 10, 'VOCÊ GANHOU!', '=' * 10)