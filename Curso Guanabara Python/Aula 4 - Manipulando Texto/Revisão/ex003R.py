# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o nome da cidade: ').strip().lower()

print(f'O nome da cidade contem "Santo"? {"santo" in cidade}')