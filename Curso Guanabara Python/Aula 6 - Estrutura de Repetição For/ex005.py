# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
numero_2 = 0

for c in range(1, 7):
    numero = int(input(f'Digite o {c}° numero: '))
    if numero % 2 == 0:
        numero_2 += numero
print(f'A soma dos numeros pares é {numero_2}')