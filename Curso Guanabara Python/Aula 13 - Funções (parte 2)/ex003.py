# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador= 'Desconhecido', gols= 0):
    print(f'O jogador {jogador} fez {gols} gols no campeonato.')

jogador = input('Nome do jogador: ')
gols = input('Numero de gols no campeonato: ')

if gols.isnumeric():
    int(gols)
    if jogador == '':
        ficha(gols= gols)
    else:
        ficha(jogador, gols)
else:
    ficha(jogador)
    if jogador == '':
        ficha()
