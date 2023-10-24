from random import choice

nome_1 = input('Digite o primeiro nome: ')
nome_2 = input('Digite o segundo nome: ')
nome_3 = input('Digite o terceiro nome: ')
nome_4 = input('Digite o quarto nome: ')
lista = [nome_1, nome_2, nome_3, nome_4]
print(f'O aluno escolhido foi {choice(lista)}!')