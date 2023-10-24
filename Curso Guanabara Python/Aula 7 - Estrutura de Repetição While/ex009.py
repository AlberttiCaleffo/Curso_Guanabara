# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = int(input('Digite um numero: '))
parada = input('Quer continuar? [S/N] ').upper()
media = numero
contador = 1
maior = menor = numero

while parada == 'S':
    numero = int(input('Digite outro numero: '))
    parada = input('Quer continuar? [S/N] ').upper().strip()
    media += numero
    if numero > maior:
        maior = numero
    else:
        menor = numero
    contador += 1
print(f'Você digitou os numeros solicitados {contador} vezes. A media deles é {media / contador:.2f}\n'
      f'O menor valor é {menor} e o maior é {maior}')