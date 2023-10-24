# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

conjunto = (int(input('Digite um numero: ')),
            int(input('Digite outro numero: ')),
            int(input('Digite mais um numero: ')),
            int(input('Digite o ultimo numero: ')))
          
print(f'Os valores obtidos foram: {conjunto}')
print(f'O numero 9 apareceu {conjunto.count(9)} vez(es).' if 9 in conjunto else 'Não a numero 9.')
print(f'O numero 3 apareceu na {conjunto.index(3) + 1}° posição.' if 3 in conjunto else 'Não a numero 3.')

for par in conjunto:
    if par % 2 == 0:
        print(f'O numero par é {par}')
        break
    else:
        continue