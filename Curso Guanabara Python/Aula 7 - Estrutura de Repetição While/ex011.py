# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 12)
print('Jogo Par ou Impar!')
print('=-' * 12)

mao_jogador = int(input('Qual sera sua jogada: [1 a 10]: '))
mao_computador = randint(1, 10)
decisao = input('Você escolhe Impar ou Par? [P/I]: ').lower().strip()
resultado = mao_jogador + mao_computador
vencido = 0

while True:
    if resultado % 2 == 0 and decisao in 'p' or resultado % 2 == 1 and decisao in 'i':
        print(f'Você escolheu {mao_jogador} e o computador escolheu {mao_computador}. A soma dos dois deu {resultado}.')
        print('Deu PAR. Você GANHOU!' if resultado % 2 == 0 else 'Deu IMPAR. Você GANHOU!')
    else:
        print(f'Você escolheu {mao_jogador} e o computador escolheu {mao_computador}. A soma dos dois deu {resultado}.')
        print('Deu PAR. Você PERDEU!' if resultado % 2 == 0 else 'Deu IMPAR. Você PERDEU!')
        break
    mao_jogador = int(input('Qual vai ser a proxima jogada: [1 a 10]: '))
    mao_computador = randint(1, 10)
    decisao = input('Você escolheu Impar ou Par? [P/I]: ').lower().strip()
    resultado = mao_jogador + mao_computador
    vencido += 1

print(f'Fim do jogo. Você venceu {vencido}.')
