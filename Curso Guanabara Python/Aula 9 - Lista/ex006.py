# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
# expressao = input('Digite uma expressão: ')

# if expressao.count('(') == expressao.count(')'):
# print('A expressão é \033[32mVALIDA!\033[32m')
# else:
# print('A expressão é \033[31mINVALIDA.\033[31m')

expressao = input('Digite uma expressão: ')
parenteses = []

for individual in expressao:
    parenteses.append(individual)

while '(' in parenteses or ')' in parenteses:
    if parenteses.index('(') > parenteses.index(')') or parenteses.count('(') != parenteses.count(')'):
        print('Operação incorreta!')
        break
    elif '(' in parenteses and ')' in parenteses:
        del parenteses[parenteses.index('(')]
        del parenteses[parenteses.index(')')]
        if parenteses.count('(') == 0 and parenteses.count(')') == 0:
            print('Operação correta')