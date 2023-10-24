from random import randint

usuario_numero = int(input('Informe um numero de 0 a 5: '))
maquina_numero = randint(0, 5)

print('PROCESSANDO...')

if maquina_numero == usuario_numero:
    print(f'Você ganhou! Você escolheu a mesma numero que a maquina')
else:
    print(f'Você perdeu, a maquina escolheu outra numero')
