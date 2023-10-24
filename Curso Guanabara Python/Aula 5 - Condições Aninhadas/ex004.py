# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos e falta {18 - idade} anos para o alistamento. Seu alistamento sera em {18 - idade + ano_atual}')
elif idade == 18:
    print(f'Seu alistamento é este ano, faça IMEDIATAMENTE!')
else:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos e ja passou {idade - 18} anos do seu alistamento.')

