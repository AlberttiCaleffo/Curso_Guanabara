# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#                  Depois disso, mostre:
#                                  A) Quantos números foram digitados.                                                                                                                    
#                                       B) A lista de valores, ordenada de forma decrescente.                                                                                          
#                                          C) Se o valor 5 foi digitado e está ou não na lista.

conjunto = []

while True:
    numero = int(input('Digite um numero: '))
    conjunto.append(numero)
    continuar = input('Quer continuar? [S/N]: ').upper()
    if 'N' in continuar:
        break
    
print(f'Foram digitados {len(conjunto)} numeros\n'
      f'A ordem inversa é {sorted(conjunto, reverse = True)}')
print('O numero 5 aparece.' if 5 in conjunto else 'Não tem numero 5.')