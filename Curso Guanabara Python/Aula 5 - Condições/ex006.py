numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_3 = int(input('Digite o terceiro numero: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'O numero {numero_1} é o maior.')
    if numero_2 < numero_3:
        print(f'O numero {numero_2} é o menor.')
    else:
        print(f'O numero {numero_3} é o menor.')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'O numero {numero_2} é o maior')
    if numero_1 < numero_3:
        print(f'O numero {numero_1} é o menor.')
    else: 
        print(f'O numero {numero_3} é o menor.')
else:
    print(f'O numero {numero_3} é o maior')
    if numero_2 < numero_1:
        print(f'O numero {numero_2} é o menor.')
    else:
        print(f'O numero {numero_1} é o menor.')
