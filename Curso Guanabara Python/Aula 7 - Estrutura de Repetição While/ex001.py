# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

#    sexo = int(input('Digite o sexo do individuo: [1] masculino [2] feminino '))

#    while sexo != 1 and sexo != 2:
#        print('Caractere invalido, digite novamente: ')
#        sexo = int(input('Digite o sexo novamente: '))
#    print(f'O sexo do individuo é {str(sexo)}'.replace('1', 'masculino').replace('2', 'feminino'))

#    sexo = input('Digite o sexo do individuo: [m] masculino [f] feminino ').upper().strip()

#    while sexo != 'M' and sexo != 'F':
#        print('Caractere invalido, digite novamente: ')
#        sexo = input('Digite o sexo novamente: ').upper().strip()
#    if sexo == 'M':
#        print('O sexo do individuo é masculino.')
#    else:
#        print('O sexo do individuo é feminino.')

sexo = input('Digite o sexo do individuo: [M] Masculino [F] Feminino ').upper().strip()

while sexo not in 'MF':
    sexo = input('Caractere incorreto. Digite novamente: ').upper().strip()
if sexo in 'M':
    print('Sexo masculino inserido com sucesso!')
else:
    print('Sexo feminino inserido com sucesso!')