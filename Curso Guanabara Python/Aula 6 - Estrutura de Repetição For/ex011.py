# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
idade_mais_velho = 0
numero_de_mulheres = 0

for c in range(1, 5):
    nome = input(f'Digite o {c}° nome: ')
    idade = int(input(f'Digite a idade do(a) {nome}: '))
    sexo = input('Qual o sexo? [M] Masculino [F] Feminino ').lower()
    media += idade
    if sexo == 'm':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome
        else:
            continue
    elif sexo == 'f':
        if idade < 20:
            numero_de_mulheres += 1
        else:
            continue
print(f'A media de idade é {media / 4:.1f}. '
      f'O nome do homem mais velho é {nome_mais_velho} com {idade_mais_velho}. '
      f'Temos {numero_de_mulheres} mulher(es) menores que 20 anos.')
        