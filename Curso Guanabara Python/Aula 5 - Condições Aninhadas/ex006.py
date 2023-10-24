# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER

from datetime import datetime

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = datetime.now().year - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos.\nEle é um atleta MIRIM!')
elif idade <= 14 and idade > 9:
    print(f'O atleta tem {idade} anos.\nEle é um atleta INFANTIL')
elif idade <= 19 and idade > 14:
    print(f'O atleta tem {idade} anos.\nEle é um atleta JUNIOR')
elif idade <= 25 and idade > 19:
    print(f'O atleta tem {idade} anos.\nEle é um atleta SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.\nEle é um atleta MASTER')