# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero de 0 a 9999: '))

print(f'Milhar: {numero // 1000} Centena: {numero % 1000 // 100} Dezena: {numero % 1000 % 100 // 10} Unidade: {str(numero)[-1]}')