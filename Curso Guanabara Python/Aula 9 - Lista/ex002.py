# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

conjunto = []

while True:
    numero = int(input('Digite um numero: '))
    if numero in conjunto:
        print('Numero ja existe. Insira novamente...')
    else:
        conjunto.append(numero)
        print('Numero adicionado com sucesso!')
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if 'N' in continuar:
        break       
print(f'A sequencia em ordem crescente é: {sorted(conjunto)}')