# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
contador = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print(f'As vezes que aparece os numeros solicitados é {contador} e a soma de todos eles é {soma}')
