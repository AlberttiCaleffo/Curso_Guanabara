# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados_funcionario = {}

dados_funcionario['nome'] = input('Digite o nome do funcionario: ')
dados_funcionario['ano_nascimento'] = int(input('Ano de nascimento: '))
dados_funcionario['idade'] = date.today().year - dados_funcionario['ano_nascimento']
dados_funcionario['carteira_trabalho'] = int(input('Carteira de trabalho (0 caso não tenha): '))

if dados_funcionario['carteira_trabalho'] == 0:
    print('=-' * 30)
    for v, k in dados_funcionario.items():
        print(f'{v} tem o valor {k}')
else:
    dados_funcionario['contratacao'] = int(input('Data de contratação: '))
    dados_funcionario['salario'] = float(input('Informe o salario: R$'))
    dados_funcionario['aposentadoria'] = dados_funcionario['contratacao'] - dados_funcionario['ano_nascimento'] + 35
    for v, k in dados_funcionario.items():
        print(f'   - {v} tem o valor {k}')

