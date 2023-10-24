# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

print(f'''\
      Seu nome com letras minusculas: {nome.lower()}
      Seu nome com letras maisculas: {nome.upper()}
      Seu nome tem {len(''.join(nome.split()))} caracteres
      Seu nome tem {len(nome)} caracteres com espaços
      Seu primeiro nome tem {len(nome.split()[0])} caracteres''')  
