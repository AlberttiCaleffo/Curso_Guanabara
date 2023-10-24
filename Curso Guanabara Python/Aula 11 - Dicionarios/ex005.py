# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

cadastro = {}
dados = []
dados_m_maior = []
dados_f_maior = []
continuar = 'S'
media = m_maior = f_maior = 0


while 'S' in continuar:
    cadastro['nome'] = input('Digite o nome da pessoa: ')
    cadastro['sexo'] = input('Qual o genero? [M/F] ').upper()

    while cadastro['sexo'] not in ['M', 'F']:
        cadastro['sexo'] = input('Genero invalido. Digite um valido: [M/F] ').upper()

    cadastro['idade'] = int(input(f'Digite a idade de {cadastro["nome"]}: '))

    dados.append(cadastro.copy())
    cadastro.clear()
    continuar = input('Quer continuar? [S/N] ').upper()

    while continuar not in ['S', 'N']:
        continuar = input('Valor invalido, digite novamente: [S/N] ').upper()

print('-=' * 30)    
print(f'Foram cadastradas {len(dados)} pessoas no banco de dados.')

for contador in range(len(dados)):
    media += dados[contador]["idade"]
    
print(f'A media de idade é {media / len(dados):.2f}')

print('As mulheres que temos são ', end= '')
for contador in range(len(dados)):
    if dados[contador]['sexo'] == 'F':
        print(dados[contador]['nome'], end = ' ')
print()
        
for contador in range(len(dados)):
    if dados[contador]['idade'] > m_maior and dados[contador]['sexo'] == 'M':
        m_maior = dados[contador]['idade']
        dados_m_maior = dados[contador]
    elif dados[contador]['idade'] > f_maior and dados[contador]['sexo'] == 'F':
        f_maior = dados[contador]['idade']
        dados_f_maior = dados[contador]
        
print('As pessoas que estam acima da media são:')
print(end= '-    ')
for k, v in dados_m_maior.items():
    print(f'{k} = {v}', end= '; ')
print()
print(end= '-    ')
for k, v in dados_f_maior.items():
    print(f'{k} = {v}', end= '; ')
print()