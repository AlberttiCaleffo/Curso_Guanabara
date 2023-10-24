# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

nome_aluno = []
notas = []
nome_notas = []
contador = numero_aluno = 0
while True:
    nome_aluno.append(input('Nome: ').title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nome_notas.append(nome_aluno[:])
    nome_notas[contador].append(notas[:])
    nome_aluno.clear()
    notas.clear()
    continuar = input('Quer continuar? [S/N] ').upper()
    contador += 1
    if 'N' in continuar:
        break
print('No.', ' ' * 5, 'NOME', ' ' * 5, 'MEDIA', ' ' * 5)
print('-' * 30)
for lista_alunos in nome_notas:
    print(f'{numero_aluno:<9}', f'{lista_alunos[0]:<10}', f'{(lista_alunos[1][0] + lista_alunos[1][1]) / 2:.1f}')
    numero_aluno += 1
print('-' * 30)
while True:
    consulta = int(input('Qual o numero do aluno a qual você quer as notas? [999 interrompe] '))
    if consulta == 999:
        break
    print(f'Notas de {nome_notas[consulta][0]} é {nome_notas[consulta][1]}')
    print('-' * 30)
print('=' * 30)
print('Programa Finalizado.')