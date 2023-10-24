# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = []
par = []
impar = []

for c in range(0, 7):
    numeros.append(int(input(f'Digite o {c + 1} numero: ')))
    if numeros[0] % 2 == 0:
        par.append(numeros[0])
        numeros.clear()
    else:
        impar.append(numeros[0])
        numeros.clear()

numeros.append(par[:])
numeros.append(impar[:])
numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares foram: {numeros[0]}\n',
      f'Os valores impares foram: {numeros[1]}')