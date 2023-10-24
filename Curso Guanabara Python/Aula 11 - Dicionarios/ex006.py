# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados_jogadores = []
jogadores = {}
gols = []
partidas = []
continuar = 'S'
contador = 0

while 'S' in continuar:
    partidas.clear()
    jogadores['nome'] = input('Digite o nome do jogador: ').title()
    partidas.append(int(input(f'Quantos jogos o {jogadores["nome"]} fez? ')))
    
    for c in range(partidas[0]):
        gols.append(int(input(f'Quantos gols fez no {c + 1} jogo? ')))
        
    jogadores['gols'] = gols.copy()    
    dados_jogadores.append(jogadores.copy())
    jogadores.clear()
    gols.clear()
    contador += 1
    continuar = input('Quer continuar? [S/N] ').upper()

print('-=' * 30)
print('Cod', 'Nome', '     Gols', '           Total\n', '-' * 30)    
for c in range(contador): 
    if c == len(dados_jogadores):
        break 
    print(c, end= ' ')
    for v in dados_jogadores[c].values():
        print(f'  {str(v):<7}', end= ' ')
    print(f'{sum(dados_jogadores[c]["gols"]):>10}')
print('-' * 30)
print('-=' * 30)    
while True:
    banco_de_dados = int(input('Gostaria de obter o dado de algum jogador em especifico? [999 para parar] '))
    if banco_de_dados == 999:
        break
    print(f'Levantamento dos jogos de {dados_jogadores[banco_de_dados]["nome"]}:')
    for c in range(len(dados_jogadores[banco_de_dados]['gols'])):
        print(f'No jogo {c + 1} fez {dados_jogadores[banco_de_dados]["gols"][c]} gols')