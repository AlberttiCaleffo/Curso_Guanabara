# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_par = []
lista_impar = []
conjunto = []

while True:
    numero = int(input('Digite um numero: '))
    conjunto.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if 'N' in continuar:
        break

print(f'Os numeros digitados foram: {conjunto}\n'
      f'Os numeros pares são: {lista_par}\n'
      f'Os numeros impares são: {lista_impar}')
