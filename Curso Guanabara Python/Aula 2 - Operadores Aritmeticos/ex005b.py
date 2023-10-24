numero = int(input('Digite um numero: '))

for a in range(1, 11):
    print(f'{numero:>2} x {a:>2} = {numero * a:>2}')
print('=' * 15)
for a in range(1, 11):
    print(f'{numero - 1:>2} x {a:>2} = {(numero - 1) * a:>2}')