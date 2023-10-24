# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

numero = int(input('Insira um numero de 0 a 100: '))
computador = randint(0, 100)
erros = 0

while numero not in range(0, 101):
    numero = int(
        input('Numero invalido. Insira novamente um numero de 0 a 100: '))
while numero != computador:
    if numero > computador:
        numero = int(input('Errou... Um pouco menos. Tente novamente: '))
    else:
        numero = int(input('Errou... Um pouco mais. Tente novamente: '))
    erros += 1

print(
    f'Você ACERTOU! Escolhi o numero {computador}. Você errou {erros} vezes.')
