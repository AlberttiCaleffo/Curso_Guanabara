# Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(numero= input('Digite um numero: '.strip())):
    while True:
        if numero.isnumeric():
            return numero
        else:
            print('\033[31mERRO! O numero digitado não é um numero valido. Digite um valido.\033[31m')
            numero = input('Digite um numero valido: ')
            if numero.isnumeric():
                return numero

print(leiaInt())