# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

print('-=' * 10,
      'Cadastre uma pessoa.',
      '-=' * 10)

continuar = ''
maiores_de_18 = homens_cadastrados = mulheres_menos_20 = 0

while True:
    idade = int(input('Quantos anos tem: '))
    sexo = input('Qual o genero? [M/F]: ')
    maiores_de_18 += 1 if idade > 18 else 0
    homens_cadastrados += 1 if sexo == 'm' else 0
    mulheres_menos_20 += 1 if sexo == 'f' and idade > 20 else 0
    continuar = input('Quer continuar? [S/N]: ').lower().strip()
    if continuar == 'n':
        break
print(f'Foram cadastrados {maiores_de_18} pessoa(s) maiores de 18.\n'
      f'Foram cadastrados {homens_cadastrados} homem(s).\n'
      f'Foram cadastrados {mulheres_menos_20} mulher(s) menores de 20.')
