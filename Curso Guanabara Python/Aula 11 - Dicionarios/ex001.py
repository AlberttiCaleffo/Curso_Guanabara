# Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados_aluno = {}

dados_aluno['Nome'] = input('Digite o nome do aluno: ').title()
dados_aluno['Nota'] = float(input(f'Digite a média do aluno {dados_aluno["Nome"]}: '))

if dados_aluno['Nota'] >= 7:
    dados_aluno['Situacao'] = 'APROVADO!'
elif dados_aluno['Nota'] >= 5 and dados_aluno['Nota'] < 7:
    dados_aluno['Situacao'] = 'RECUPERAÇÃO!'
else:
    dados_aluno['Situacao'] = 'REPROVADO!'

print('=-' * 30)

for k, v in dados_aluno.items():
    print(f'{k} é igual a {v}')

# print(f'- O nome é {dados_aluno["nome"]}\n'
#      f'- A média de {dados_aluno["nome"]} é {dados_aluno["nota"]}\n'
#      f'- A situação dele é igual a {dados_aluno["situacao"]}')