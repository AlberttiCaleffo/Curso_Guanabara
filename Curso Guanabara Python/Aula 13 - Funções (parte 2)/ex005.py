# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber 
# várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)

def notas(*nota, sit= False):
    dados = {}
    dados['total'] = len(nota)
    dados['maior'] = max(nota)
    dados['menor'] = min(nota)
    dados['media'] = f'{sum(nota) / len(nota):.2f}'
    situacao = ''
    if float(dados['media']) < 5:
        situacao = 'Ruim'
    elif float(dados['media']) >= 5 and float(dados['media']) < 7:
        situacao = 'Rasoavel'
    else:
        situacao = 'Bom'
    if sit:
        dados['situação'] = situacao
    return dados

print(notas(5.5, 9.5, 10, 6.5, sit= True))
