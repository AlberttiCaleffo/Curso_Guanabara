# Exercício Python 101: Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))

def voto(ano):
    ano = date.today().year - nascimento
    if ano < 16:
        return f'Não esta apto a votar.'
    elif ano > 16 and ano < 18 or ano > 70:
        return 'Seu voto é opcional.'
    else:
        return f'Seu voto é obrigatorio!'
    
print(f'Você tem {date.today().year - nascimento} anos. {voto(nascimento)}')
