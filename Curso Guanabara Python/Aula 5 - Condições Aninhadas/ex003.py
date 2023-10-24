numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

if numero_1 > numero_2:
    print(f'O {numero_1} é MAIOR que o {numero_2}')
elif numero_1 == numero_2:
    print(f'O {numero_1} é IGUAL ao {numero_2}')
else:
    print(f'O {numero_2} é MAIOR que o {numero_1}')
