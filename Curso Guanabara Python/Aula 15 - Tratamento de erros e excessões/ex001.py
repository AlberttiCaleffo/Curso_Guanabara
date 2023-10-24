# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(numero= 0):
    while True:        
        try:
            numero = int(input('Digite um numero inteiro: '))
            return numero
        except (ValueError):
            print('Erro! O numero digitado não é um inteiro.')

def leiaFloat(numero= 0):
    while True:
        try:
            numero = float(input('Digite um numero real: '))
            return numero
        except:
            print('Erro, numero invalido!')

print(f'O numero inteiro é {leiaInt()} e o numero real é {leiaFloat()}')