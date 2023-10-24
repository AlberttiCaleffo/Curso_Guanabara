termos = int(input('Quantos termos você quer mostra: '))
contador = 0
sequencia_atual = 1
sequencia_anterior = -1

while contador < termos:
    if contador % 2 == 0:
        sequencia_anterior = sequencia_anterior + sequencia_atual
        print(f'{sequencia_anterior}', end=' -> ')
    else:
        sequencia_atual = sequencia_anterior + sequencia_atual
        print(f'{sequencia_atual}', end=' -> ')
    contador += 1
print('Fim')
