numero = int(input('Digite um numero: '))
contador1 = 1
contador2 = 1

while contador1 < 11:
    print(f'{numero:>2} x {contador1:>2} = {numero * contador1:>2}')
    contador1 += 1
print('=' * 15)
while contador2 < 11: 
    print(f'{numero - 1:>2} x {contador2:>2} = {(numero - 1) * contador2:>2}')
    contador2 += 1