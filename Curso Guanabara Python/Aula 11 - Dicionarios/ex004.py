# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
contador = contador2 = 1

jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
partidas = jogador['partidas']

while jogador['partidas'] != 0:
    gols.append(int(input(f'Quantos gols na partida {contador}? ')))
    jogador['gols'] = gols
    jogador['total_gols'] = sum(jogador['gols'])
    jogador['partidas'] -= 1
    contador += 1
del jogador['partidas']

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
while contador2 <= partidas:
    print(f'=> Na partida {contador2}, fez {jogador["gols"][contador2 - 1]} gols.')
    contador2 += 1
print(f'Foi um total de {jogador["total_gols"]} gols.')