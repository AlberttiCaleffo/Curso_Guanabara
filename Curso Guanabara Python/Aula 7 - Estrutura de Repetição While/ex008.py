# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = soma = numero = 0

while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero != 999:
        soma += numero
        contador += 1
    elif numero == 999:
        break

print(
    f'Você digitou {contador} vezes. A soma dos numeros digitados foi {soma}')
