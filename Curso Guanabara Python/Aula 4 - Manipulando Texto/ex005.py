frase = input('Digite uma frase: ').strip().lower()

print('A sua frase tem {} "A".'.format(frase.count('a')))
print('O primeiro "A" se encontra na posição {}'.format(frase.find('a')))
print('O ultimo "A" se encontra na posição {}'.format(frase.rfind('a')))