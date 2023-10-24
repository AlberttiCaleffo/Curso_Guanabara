# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

numero = int(input('Digite um numero a qual vai ser dado a tabuada: '))

while True:
    print('-=' * 10)
    for c in range(1, 11):
        print(f'{numero:<2} x {c:<2} = {numero * c:<2}')
    print('-=' * 10)
    numero = int(input('Digite outro numero: '))
    if numero <= 0:
        break

print('Programa encerrado!')
